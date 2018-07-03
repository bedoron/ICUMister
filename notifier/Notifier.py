from verification.FaceVerification import FaceVerificationResult
from abc import ABCMeta, abstractmethod
from logging import Logger

class Notifier(object):
    __metaclass__ = ABCMeta

    def __init__(self, logger):
        """
        :type logger: Logger
        """
        super(Notifier, self).__init__()
        self._logger = logger

    @abstractmethod
    def notify(self, face_verification_result):
        """
        Notify user
        :type face_verification_result: FaceVerificationResult
        :return:
        """
        raise NotImplementedError()
