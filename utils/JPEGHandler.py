from identification.FaceIdentification import FaceIdentification
from notifier.Notifier import Notifier
from verification.FaceVerification import FaceVerification
from KeyVaultFetcher import KeyVaultFetcher
import logging

class JPEGHandler(object):
    def __init__(self, face_identification, face_verification, notifier):
        """
        :type face_identification: FaceIdentification
        :type face_verification: FaceVerification
        :type notifier: Notifier
        """
        super(JPEGHandler, self).__init__()
        self._notifier = notifier
        self._face_verification = face_verification
        self._face_identification = face_identification
        self._logger = logging.getLogger("ICUMister." + __name__)

    def handle(self, jpeg_data):
        if not self._face_identification.is_face(jpeg_data):
            return

        verification_result = self._face_verification.verify_face(jpeg_data)
        if verification_result.is_verified:
            self._logger.info("Found verified face, ignoring")
            return

        self._notifier.notify(verification_result)
