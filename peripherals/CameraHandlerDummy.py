from peripherals.CameraHandler import CameraHandler
from utils.FileContainer import FileContainer


class DummyFileContainer(FileContainer):
    def __init__(self, fname):
        super(DummyFileContainer, self).__init__()
        self._fname = fname

    def read(self):
        with open(self._fname, 'rb') as f:
            return f.read()


class CameraHandlerDummy(CameraHandler):
    def get_mjpeg(self):
        return DummyFileContainer('c:\\test\\roger.jpg')

    def _setup_camera(self):
        pass

    def _shutdown_camera(self):
        pass
