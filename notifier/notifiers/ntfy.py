import requests
from notifier.notifiers.notifier_interface import Notifier


class NTFYNotifier(Notifier):

    def __init__(self, url, proxy):
        self._url = url
        self._proxy = proxy

    def send_notification(self, headers, data):
        try:
            response = requests.post(url=self._url, headers=headers, data=data)
            if response.status_code == 200:
                return {"status": "success"}
            else:
                return {"status": "error", "message": response.text}
        except Exception as ex:
            return {"status": "error", "message": str(ex)}
