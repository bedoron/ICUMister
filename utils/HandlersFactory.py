from detection.FaceDetectionDummy import FaceDetectionDummy
from detection.FaceDetectionREST import FaceDetectionREST
from notifier.NotifierDummy import NotifierDummy
from peripherals.CameraHandlerDummy import CameraHandlerDummy
from identification.FaceIdentificationDummy import FaceIdentificationDummy
from identification.FaceIdentificationREST import FaceIdentificationREST


class HandlersFactory(object):
    @staticmethod
    def create_pipeline_dummies():
        """
        :return:
        """
        return FaceDetectionDummy(), FaceIdentificationDummy(), NotifierDummy()

    @staticmethod
    def create_pipeline_rest():
        return FaceDetectionREST(), FaceIdentificationREST(), NotifierDummy()

    @staticmethod
    def create_camera_dummy():
        return CameraHandlerDummy()
