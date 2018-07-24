from peripherals.CameraHandler import CameraHandler
from utils.FileContainer import FileContainer
import cv2


class OCVFileContainer(FileContainer):
    def __init__(self, fname):
        super(OCVFileContainer, self).__init__()
        self._fname = fname

    def get_name(self):
        return self._fname

    def read(self):
        with open(self._fname, 'rb') as f:
            return f.read()


class CameraHandlerOCV(CameraHandler):
    def __init__(self, config_json):
        super(CameraHandlerOCV, self).__init__(config_json)
        self.video_capture = cv2.VideoCapture(0)
        self.frame = None
        self.cascPath = 'peripherals/haarcascades/haarcascade_frontalface_default.xml'
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)
        self._tmp_jpg_file_name = 'tmp.jpg'
        self._tmp_file_file_name_container = OCVFileContainer(self._tmp_jpg_file_name)
        self._sleep_sec = 10

    def is_face(self, face_image):
        gray = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        if len(faces):
            self._logger.info("OpenCV identified face at: %s", faces)
            return True
        return False

    def get_next_image(self):
        with self as s:
            while self._can_run:
                self.frame = s.get_frame()
                if self.is_face(self.frame):
                    yield s.get_mjpeg()

    def get_frame(self):
        ret, frame = self.video_capture.read()
        return frame

    def get_mjpeg(self):
        cv2.imwrite(self._tmp_file_file_name_container.get_name(), self.frame)  # save frame as JPEG file
        jpeg_data = self._tmp_file_file_name_container
        return jpeg_data

    def _setup_camera(self):
        pass

    def _shutdown_camera(self):
        pass
