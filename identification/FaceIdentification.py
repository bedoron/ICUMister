"""
This Object deals with face identification
"""
from abc import ABCMeta, abstractmethod
import logging


class FaceIdentification(object):
    __metaclass__ = ABCMeta

    def __init__(self,):
        super(FaceIdentification, self).__init__()
        self._logger = logging.getLogger("ICUMister." + __name__)

    @abstractmethod
    def is_face(self, face_image):
        """
        check if the image is an actual face, if so, return true otherwise false
        :rtype: bool
        """
        raise NotImplementedError()
