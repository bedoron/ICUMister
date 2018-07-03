from notifier.Notifier import Notifier


class NotifierDummy(Notifier):
    def notify(self, face_verification_result):
        self._logger.info("Wazzzzzuuuppppppp!!!!")

