from JPEGHandler import JPEGHandler
from KeyVaultFetcher import KeyVaultFetcher
from peripherals.CameraHandler import CameraHandler
import cognitive_face as CF


class AppRunner(object):
    def __init__(self, config, camera_factory, pipeline_factory):
        super(AppRunner, self).__init__()
        self._config = config
        self._kv = KeyVaultFetcher(self._config)
        self.configure_cf(config, self._kv)

        self._jpeg_handler = JPEGHandler(config, pipeline_factory)
        self._camera_handler = camera_factory()  # type: CameraHandler

    @staticmethod
    def configure_cf(config, kv):
        """
        Configure cognitive_face
        :type config: dict
        :type kv: KeyVaultFetcher
        """
        cf_config = config.get('cognitive_face')
        cf_secret = kv.get_secret(cf_config.get('kv_id'))

        CF.Key.set(cf_secret)
        CF.BaseUrl.set(cf_config.get('endpoint'))

    def stop(self):
        self._camera_handler.stop()
        while self._camera_handler.is_running:
            pass

    def run(self):
        for jpeg in self._camera_handler.get_next_image():
            self._jpeg_handler.handle(jpeg)
