from identification.FaceIdentification import FaceIdentification
from notifier.Notifier import Notifier
from peripherals.CameraHandler import CameraHandler
from verification.FaceVerification import FaceVerification
from logging import Logger


# TODO: Add logger
class AppRunner(object):
    def __init__(self):
        super(AppRunner, self).__init__()

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
