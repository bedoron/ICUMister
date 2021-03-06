from detection.FaceDetection import FaceDetection
from notifier.Notifier import Notifier
from identification.FaceIdentification import FaceIdentification
import logging
import time


class JPEGHandler(object):
    def __init__(self, config, pipeline_supplier, error_handler):
        """
        :param error_handler:
        :type pipeline_supplier: callabe
        """
        super(JPEGHandler, self).__init__()
        self._logger = logging.getLogger("ICUMister." + __name__)

        face_detection, face_identification, notifier = pipeline_supplier(config)

        self._notifier = notifier  # type: Notifier
        self._face_identification = face_identification  # type: FaceIdentification
        self._face_detection = face_detection  # type: FaceDetection
        self._error_handler = error_handler
        self._sleep_sec = 3

    def handle(self, jpeg_data):
        try:
            face_detection_result = self._face_detection.detect_faces_from_jpeg(jpeg_data)
            if len(face_detection_result) == 0:
                self._logger.error("Faces detected locally but not identified by FaceDetection")
                return

            identification_result = self._face_identification.identify_face(jpeg_data, face_detection_result)
            if identification_result.is_identified:
                self._logger.info("Found detected face, ignoring")
                return

            self._notifier.notify(identification_result)
            self._logger.info("Sleeping for {}".format(self._sleep_sec))
            time.sleep(self._sleep_sec)

        except Exception as e:
            self._error_handler(e)
