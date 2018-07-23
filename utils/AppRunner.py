import logging
import sys

from cognitive_face import CognitiveFaceException

from JPEGHandler import JPEGHandler
from KeyVaultFetcher import KeyVaultFetcher
from peripherals.CameraHandler import CameraHandler
import cognitive_face as CF


class AppRunner(object):
    def __init__(self, config, camera_factory, pipeline_factory):
        super(AppRunner, self).__init__()
        self._config = config
        self._logger = logging.getLogger("ICUMister." + __name__)

        self._kv = KeyVaultFetcher()

        self.configure_cf(config, self._kv)

        self._jpeg_handler = JPEGHandler(config, pipeline_factory, self.error_handler)
        self._camera_handler = camera_factory(config)  # type: CameraHandler

    @staticmethod
    def configure_cf(config, kv):
        """
        Configure cognitive_face
        :type config: dict
        :type kv: KeyVaultFetcher
        """
        cf_config = config.get('cognitive_face', {})
        cf_secret = kv.get_secret(cf_config.get('kv_id'))

        CF.Key.set(cf_secret)
        CF.BaseUrl.set(cf_config.get('endpoint'))

        # Now make sure/create personGroup
        pg_config = cf_config.get('person_group', {})
        try:
            CF.person_group.get(pg_config.get('id'))
        except CognitiveFaceException as e:
            CF.person_group.create(pg_config.get('id'), pg_config.get('name'))
        finally:
            CF.person_group.get(pg_config.get('id'))  # Make sure the group was created.

    @property
    def cognitive_face(self):
        return self._config.get('cognitive_face', {})

    @property
    def person_group(self):
        return self.cognitive_face.get('person_group', {})

    def error_handler(self, exception):
        """
        :type exception: Exception
        """
        self._logger.error("%s Failure: %s", type(exception), exception)
        if type(exception) is CognitiveFaceException:
            CF.person_group.train(self.person_group.get('id'))
        else:
            sys.exit(-1)

    def stop(self):
        self._camera_handler.stop()
        while self._camera_handler.is_running:
            pass

    def run(self):
        for jpeg in self._camera_handler.get_next_image():
            self._jpeg_handler.handle(jpeg)
