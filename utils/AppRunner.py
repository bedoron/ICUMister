from peripherals.CameraHandler import CameraHandler
from KeyVaultFetcher import KeyVaultFetcher
from JPEGHandler import JPEGHandler
from logging import Logger


class AppRunner(object):
    def __init__(self, config):
        super(AppRunner, self).__init__()
        self._config = config
        self._kv = KeyVaultFetcher(self._config)

    def initialize(self):
        self._face_api_key = self._kv.get_secret('faceKey1')

    def run(self, camera_handler, jpeg_handler):
        """
        :type camera_handler: CameraHandler
        :type jpeg_handler: JPEGHandler
        :return:
        """
        for jpeg in camera_handler.get_next_image():
            jpeg_handler.handle(jpeg)
