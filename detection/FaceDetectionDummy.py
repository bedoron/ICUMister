from detection.FaceDetection import FaceDetection


class FaceDetectionDummy(FaceDetection):
    def detect_faces_from_jpeg(self, face_image):
        self._logger.info("Identified face")
        return list({"faceId":"acd223-acd33"})
