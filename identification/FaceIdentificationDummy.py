from identification.FaceIdentification import FaceIdentification


class FaceIdentificationDummy(FaceIdentification):
    def is_face(self, face_image):
        self._logger.info("Identified face")
        return True
