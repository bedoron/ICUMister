from identification.FaceIdentification import FaceIdentification
import cognitive_face as CF

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class FaceIdentificationREST(FaceIdentification):
    def is_face(self, face_image):
        result = CF.face.detect(face_image, face_id=True)

        if len(result) > 0:
            self._logger.info("Identified face at: %s", result)

        return result
