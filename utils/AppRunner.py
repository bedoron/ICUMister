from JPEGHandler import JPEGHandler
from KeyVaultFetcher import KeyVaultFetcher
from peripherals.CameraHandler import CameraHandler


class AppRunner(object):
    def __init__(self, config, camera_factory, pipeline_factory):
        super(AppRunner, self).__init__()
        self._config = config
        self._kv = KeyVaultFetcher(self._config)

        self._face_api_key = self._kv.get_secret('faceKey1')
        self._jpeg_handler = JPEGHandler(pipeline_factory)
        self._camera_handler = camera_factory()  # type: CameraHandler

    def stop(self):
        self._camera_handler.stop()
        while self._camera_handler.is_running:
            pass

    def run(self):
        for jpeg in self._camera_handler.get_next_image():
            self._jpeg_handler.handle(jpeg)
