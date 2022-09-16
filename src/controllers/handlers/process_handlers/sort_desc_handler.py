from .interface_process_handler import IntefaceHandler


class SortDescHandler(IntefaceHandler):
    def __init__(self, request_data, route):
        self.request_data = request_data
        self.route = route

    def will_handle(self) -> bool:
        if self.route == "/sort" and self.request_data["order"] == "desc":
            return True

        return False

    def handle(self) -> {}:
        return {"message": "order desc"}
