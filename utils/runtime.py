from peripherals.CameraHandler import CameraHandler
from logging import Logger
import sys, signal


def set_sigint(logger, camera_handler):
    """
    :type logger: Logger
    :type camera_handler: CameraHandler
    :return:
    """

    def signal_handler(signal, frame):
        logger.warn("SIGINT detected")
        if camera_handler.is_running:
            camera_handler.stop()
        else:
            logger.error("Exiting violently")
            sys.exit(-1)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGABRT, signal_handler)
