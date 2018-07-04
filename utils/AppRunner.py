from identification.FaceIdentification import FaceIdentification
from notifier.Notifier import Notifier
from peripherals.CameraHandler import CameraHandler
from verification.FaceVerification import FaceVerification
from KeyVaultFetcher import KeyVaultFetcher
from logging import Logger


class AppRunner(object):
    def __init__(self, config):
        super(AppRunner, self).__init__()
        self._config = config
        self._kv = KeyVaultFetcher(self._config)

    def initialize(self):
        self._face_api_key = self._kv.get_secret('faceKey1')
        
    def run(self, logger, camera_handler, face_identification, face_verification, notifier):
        """
        :type logger: Logger
        :type camera_handler: CameraHandler
        :type face_identification: FaceIdentification
        :type face_verification: FaceVerification
        :type notifier: Notifier
        :return:
        """
        for jpeg in camera_handler.get_next_image():
            if not face_identification.is_face(jpeg):
                continue

            verification_result = face_verification.verify_face(jpeg)
            if verification_result.is_verified:
                logger.info("Found verified face, ignoring")
                continue

            notifier.notify(verification_result)
