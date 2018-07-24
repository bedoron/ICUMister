from peripherals.CameraHandler import CameraHandler
from logging import Logger
import sys, signal
from AppRunner import AppRunner


def set_sigint(logger, app_runner):
    """
    :type logger: Logger
    :type app_runner: AppRunner
    :return:
    """

    def signal_handler(signal, frame):
        logger.warn("SIGINT detected")
        app_runner.stop()
        sys.exit(-1)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGABRT, signal_handler)
