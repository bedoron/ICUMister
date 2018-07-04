import cognitive_face as CF
import urllib3

from verification.FaceVerification import FaceVerification, FaceVerificationResult

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class FaceVerificationREST(FaceVerification):
    def verify_face(self, face_image, face_identification_result):
        face_ids = [result['faceId'] for result in face_identification_result]
        result = CF.face.identify(face_ids)  # This is probably the wrong API call

        self._logger.info("Face verification result: %s", result)
        return FaceVerificationResult(result, False, face_image)
