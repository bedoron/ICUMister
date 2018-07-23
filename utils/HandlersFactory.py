from detection.FaceDetectionDummy import FaceDetectionDummy
from detection.FaceDetectionREST import FaceDetectionREST
from notifier.NotifierDummy import NotifierDummy
from peripherals.CameraHandlerDummy import CameraHandlerDummy
from identification.FaceIdentificationDummy import FaceIdentificationDummy
from identification.FaceIdentificationREST import FaceIdentificationREST


class HandlersFactory(object):
    @staticmethod
    def create_pipeline_dummies(config_json):
        """
        :return:
        """
        return FaceDetectionDummy(config_json), FaceIdentificationDummy(config_json), NotifierDummy(config_json)

    @staticmethod
    def create_pipeline_rest(config_json):
        return FaceDetectionREST(config_json), FaceIdentificationREST(config_json), NotifierDummy(config_json)

    @staticmethod
    def create_camera_dummy(config_json):
        return CameraHandlerDummy(config_json)
