from identification.FaceIdentification import FaceIdentificationResult
from notifier.Notifier import Notifier
from NotificationHub import NotificationHubClient
from utils.KeyVaultFetcher import KeyVaultFetcher
import datetime


class NotifierREST(Notifier):
    def __init__(self, config_json):
        super(NotifierREST, self).__init__(config_json)
        self._connection_string = KeyVaultFetcher().get_secret("NOTIFICATION-HUB-CONNECTION-STRING")

    def notify(self, face_verification_result):
        """
        Notify user
        :type face_verification_result: FaceIdentificationResult
        :return:
        """
        self._logger.info("Notifying EventHub...")
        hub = NotificationHubClient(self._connection_string, "ICUMisterNotificationHub", debug=True)
        date = datetime.datetime.now();
        payload = \
            {
              "data": {
                "message": "Person recognized at doorstep!",
                "timestamp": str(date),
                "url": "https://www.cnn.com"
              }
            }
        hub.send_gcm_notification(payload)
        # raise NotImplementedError()
