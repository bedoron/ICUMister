from identification.FaceIdentification import FaceIdentification
from notifier.Notifier import Notifier
from verification.FaceVerification import FaceVerification
import logging


class JPEGHandler(object):
    def __init__(self, config, pipeline_supplier):
        """
        :type pipeline_supplier: callabe
        """
        super(JPEGHandler, self).__init__()
        self._logger = logging.getLogger("ICUMister." + __name__)

        face_identification, face_verification, notifier = pipeline_supplier()

        self._notifier = notifier  # type: Notifier
        self._face_verification = face_verification  # type: FaceVerification
        self._face_identification = face_identification  # type: FaceIdentification

    def handle(self, jpeg_data):
        face_identification_result = self._face_identification.is_face(jpeg_data)
        if len(face_identification_result) == 0:
            return

        verification_result = self._face_verification.verify_face(jpeg_data, face_identification_result)
        if verification_result.is_verified:
            self._logger.info("Found verified face, ignoring")
            return

        self._notifier.notify(verification_result)
