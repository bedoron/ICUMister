import logging
from abc import ABCMeta, abstractmethod


class FaceVerificationResult(object):
    def __init__(self, verification_result, is_verified, face_image):
        self._verification_result = verification_result
        self._is_verified = is_verified
        self._face_image = face_image

    @property
    def is_verified(self):
        """
        :rtype: bool
        """
        return self._is_verified

    @property
    def verification_result(self):
        """
        :rtype: dict
        """
        return self._verification_result


class FaceVerification(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(FaceVerification, self).__init__()
        self._logger = logging.getLogger("ICUMister." + __name__)

    @abstractmethod
    def verify_face(self, face_image, face_identification_result):
        """
        Checks if the supplied face is verified (exists in the user's database)
        :rtype: FaceVerificationResult
        """
        pass
