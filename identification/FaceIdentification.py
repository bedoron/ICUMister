import logging
from abc import ABCMeta, abstractmethod


class FaceIdentificationResult(object):
    def __init__(self, identification_result, is_identified, face_image):
        self._identification_result = identification_result
        self._is_identified = is_identified
        self._face_image = face_image

    @property
    def is_identified(self):
        """
        :rtype: bool
        """
        return self._is_identified

    @property
    def identification_result(self):
        """
        :rtype: dict
        """
        return self._identification_result


class FaceIdentification(object):
    __metaclass__ = ABCMeta

    def __init__(self, config_json):
        super(FaceIdentification, self).__init__()
        self._config_json = config_json
        self._logger = logging.getLogger("ICUMister." + __name__)

    @abstractmethod
    def verify_face(self, face_image, face_identification_result):
        """
        Checks if the supplied face is verified (exists in the user's database)
        :rtype: FaceIdentificationResult
        """
        pass
