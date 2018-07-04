from identification.FaceIdentificationDummy import FaceIdentificationDummy
from notifier.NotifierDummy import NotifierDummy
from peripherals.CameraHandlerDummy import CameraHandlerDummy
from verification.FaceVerificationDummy import FaceVerificationDummy


class HandlersFactory(object):
    @staticmethod
    def create_dummies(logger):
        """
        :param logger:
        :return:
        """
        return CameraHandlerDummy(logger), FaceIdentificationDummy(logger), FaceVerificationDummy(
            logger), NotifierDummy(logger)
