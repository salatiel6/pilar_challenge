from .interface_process_handler import IntefaceHandler


class VowelCountHandler(IntefaceHandler):
    def __init__(self, request_data, route):
        self.request_data = request_data
        self.route = route

    def will_handle(self) -> bool:
        if self.route == "/vowel_count":
            return True

        return False

    def handle(self) -> {}:
        return {"message": "vowel count"}
