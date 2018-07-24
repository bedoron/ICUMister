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
        self._tmp_jpg_file_name = 'tmp.jpg'
        self.image_size = (320, 240)
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)

    def is_face(self, face_image):
        gray = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(150, 150),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        if len(faces):
            self._logger.info("OpenCV identified face at: %s", faces)
            return True
        return False

    def get_next_image(self):
        with self as s:
            log_once = True
            while self._can_run:
                self.frame = None
                if log_once:
                    self._logger.info("OpenCV looking for faces")
                    log_once = False
                frame = s.get_frame()
                if self.is_face(frame):
                    self.frame = frame
                    log_once = True
                    yield s.get_mjpeg()

    def get_frame(self):
        #hack for raspberrypi
        for i in range(10):
            ret, frame = self.video_capture.read()
        return frame

    def get_mjpeg(self):
        # cv2.imwrite(self._tmp_jpg_file_name, cv2.resize(self.frame, self.image_size))
        cv2.imwrite(self._tmp_jpg_file_name, self.frame)
        return OCVFileContainer(self._tmp_jpg_file_name)

    def _setup_camera(self):
        pass

    def _shutdown_camera(self):
        pass
