from notifiers.ntfy import NTFYNotifier


AVAILABLE_NOTIFIERS = {
    "NTFY": NTFYNotifier
}


class NotifierFactory:

    @staticmethod
    def get_available_notifiers():
        return AVAILABLE_NOTIFIERS

    def get_notifier(self, name: str):
        try:
            return AVAILABLE_NOTIFIERS[name]
        except Exception as ex:
            raise f"{name} is not available. Error: {str(ex)}"
