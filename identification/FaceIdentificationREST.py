import cognitive_face as CF
import urllib3

from identification.FaceIdentification import FaceIdentification, FaceIdentificationResult

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class FaceIdentificationREST(FaceIdentification):
    def verify_face(self, face_image, face_identification_result):
        face_ids = [result['faceId'] for result in face_identification_result]
        result = CF.face.identify(face_ids)  # This is probably the wrong API call

        self._logger.info("Face identification result: %s", result)
        return FaceIdentificationResult(result, False, face_image)
