from peripherals.CameraHandler import  CameraHandler
import logging
import sys, signal


def set_sigint(camera_handler):
    """
    :type camera_handler: CameraHandler
    :return:
    """

    def signal_handler(signal, frame):
        logger = logging.getLogger()
        logger.warn("SIGINT detected")
        if camera_handler.is_running:
            camera_handler.stop()
        else:
            logger.error("Exiting violently")
            sys.exit(-1)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGABRT, signal_handler)



