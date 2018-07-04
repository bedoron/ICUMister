from identification.FaceIdentificationDummy import FaceIdentificationDummy
from identification.FaceIdentificationREST import FaceIdentificationREST
from notifier.NotifierDummy import NotifierDummy
from peripherals.CameraHandlerDummy import CameraHandlerDummy
from verification.FaceVerificationDummy import FaceVerificationDummy
from verification.FaceVerificationREST import FaceVerificationREST


class HandlersFactory(object):
    @staticmethod
    def create_pipeline_dummies():
        """
        :return:
        """
        return FaceIdentificationDummy(), FaceVerificationDummy(), NotifierDummy()

    @staticmethod
    def create_pipeline_rest():
        return FaceIdentificationREST(), FaceVerificationREST(), NotifierDummy()

    @staticmethod
    def create_camera_dummy():
        return CameraHandlerDummy()
