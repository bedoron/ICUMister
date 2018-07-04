from abc import ABCMeta, abstractmethod
import logging


class CameraHandler(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._can_run = True
        self._logger = logging.getLogger("ICUMister." + __name__)
        super(CameraHandler, self).__init__()

    @abstractmethod
    def get_mjpeg(self):
        """
        Returns image as base64
        :rtype: str
        """
        raise NotImplementedError()

    @abstractmethod
    def _setup_camera(self):
        raise NotImplementedError()

    @abstractmethod
    def _shutdown_camera(self):
        raise NotImplementedError()

    def stop(self):
        self._can_run = False

    @property
    def is_running(self):
        return self._can_run

    def get_next_image(self):
        with self as s:
            while self._can_run:
                yield s.get_mjpeg()

    def __enter__(self):
        """
        Initialize camera fd
        :return:
        """
        self._logger.info("Setting up camera...")
        self._setup_camera()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._logger.info("Shutting down camera...")
        self._shutdown_camera()
