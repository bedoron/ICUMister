from detection.FaceDetection import FaceDetection


class FaceDetectionDummy(FaceDetection):
    def is_face(self, face_image):
        self._logger.info("Identified face")
        return True
