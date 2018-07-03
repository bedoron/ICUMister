from peripherals.CameraHandler import CameraHandler


class CameraHandlerDummy(CameraHandler):

    def get_mjpeg(self):
        return "BlaBla".encode("base64")

    def _setup_camera(self):
        pass

    def _shutdown_camera(self):
        pass