from detection.FaceDetection import FaceDetection
import cognitive_face as CF

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class FaceDetectionREST(FaceDetection):
    def detect_faces_from_jpeg(self, face_image):
        result = CF.face.detect(face_image, face_id=True, attributes="gender,age")

        if len(result) > 0:
            self._logger.info("detected face at: %s", result)

        return result
