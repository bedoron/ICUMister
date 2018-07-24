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

        face_identification, face_verification, notifier = pipeline_supplier(config)

        self._notifier = notifier  # type: Notifier
        self._face_verification = face_verification  # type: FaceIdentification
        self._face_identification = face_identification  # type: FaceDetection
        self._error_handler = error_handler
        self._sleep_sec = 3

    def handle(self, jpeg_data):
        try:
            face_identification_result = self._face_identification.get_faces_from_jpeg(jpeg_data)
            if len(face_identification_result) == 0:
                self._logger.error("Faces detected locally but not identified by FaceDetection")
                return

            verification_result = self._face_verification.verify_face(jpeg_data, face_identification_result)
            if verification_result.is_identified:
                self._logger.info("Found verified face, ignoring")
                return
            self._notifier.notify(verification_result)

            self._logger.info("Sleeping for {}".format(self._sleep_sec))
            time.sleep(self._sleep_sec)

        except Exception as e:
            self._error_handler(e)
