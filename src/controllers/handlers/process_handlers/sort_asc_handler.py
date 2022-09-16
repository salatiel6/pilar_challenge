from .interface_process_handler import IntefaceHandler


class SortAscHandler(IntefaceHandler):
    def __init__(self, request_data, route):
        self.request_data = request_data
        self.route = route

    def will_handle(self) -> bool:
        if self.route == "/sort" and self.request_data["order"] == "asc":
            return True

        return False

    def handle(self) -> []:
        words = self.request_data["words"]
        result = sorted(words)

        return result
