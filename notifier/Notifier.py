from identification.FaceIdentification import FaceIdentificationResult
from abc import ABCMeta, abstractmethod
import logging
import NotificationHub

class Notifier(object):
    __metaclass__ = ABCMeta

    def __init__(self, config_json):
        super(Notifier, self).__init__()
        self._config_json = config_json
        self._logger = logging.getLogger("ICUMister." + __name__)

    @abstractmethod
    def notify(self, face_verification_result):
        """
        Notify user
        :type face_verification_result: FaceIdentificationResult
        :return:
        """

        raise NotImplementedError()
