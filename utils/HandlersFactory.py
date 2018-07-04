from identification.FaceIdentificationDummy import FaceIdentificationDummy
from notifier.NotifierDummy import NotifierDummy
from peripherals.CameraHandlerDummy import CameraHandlerDummy
from verification.FaceVerificationDummy import FaceVerificationDummy


class HandlersFactory(object):
    @staticmethod
    def create_dummies():
        """
        :return:
        """
        return CameraHandlerDummy(), FaceIdentificationDummy(), FaceVerificationDummy(), NotifierDummy()
