import cognitive_face as CF
import urllib3

from identification.FaceIdentification import FaceIdentification, FaceIdentificationResult

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class FaceIdentificationREST(FaceIdentification):
    def __init__(self, config_json):
        super(FaceIdentificationREST, self).__init__(config_json)
        self._pg_id = self._config_json.get('cognitive_face', {}).get('person_group', {}).get('id', None)

    def verify_face(self, face_image, face_identification_result):
        status = CF.person_group.get_status(self._pg_id)
        if status['status'] == 'failed':
            self._logger.error("PersonGroup status is failure, treating person as stranger. %s", status)
            return FaceIdentificationResult(status, False, face_image)

        face_ids = [result['faceId'] for result in face_identification_result]
        result = CF.face.identify(face_ids, self._pg_id)

        self._logger.info("Face identification result: %s", result)
        return FaceIdentificationResult(result, False, face_image)
