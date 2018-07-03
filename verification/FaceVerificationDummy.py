from verification.FaceVerification import FaceVerification
from verification.FaceVerification import FaceVerificationResult


class FaceVerificationDummy(FaceVerification):
    def verify_face(self, face_image):
        self._logger.info("Verifying some face")
        return FaceVerificationResult({"some": "result"}, False, face_image)
