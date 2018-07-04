from AppRunner import AppRunner
import logging
import sys, signal


def set_sigint(app_runner):
    """
    :type camera_handler: AppRunner
    :return:
    """

    def signal_handler(signal, frame):
        logger = logging.getLogger()
        logger.warn("SIGINT detected")
        app_runner.stop()
        sys.exit(-1)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGABRT, signal_handler)



