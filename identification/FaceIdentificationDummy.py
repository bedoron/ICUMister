from identification.FaceIdentification import FaceIdentification
from identification.FaceIdentification import FaceIdentificationResult


class FaceIdentificationDummy(FaceIdentification):
    def verify_face(self, face_image, face_identification_result):
        self._logger.info("Verifying some face")
        return FaceIdentificationResult({"some": "result"}, False, face_image)
