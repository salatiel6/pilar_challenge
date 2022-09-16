from .process_handlers import VowelCountHandler, SortAscHandler, \
    SortDescHandler


class ProcessHandler:
    def __init__(self, request_data, route):
        self.handlers = [
            VowelCountHandler(request_data, route),
            SortAscHandler(request_data, route),
            SortDescHandler(request_data, route)
        ]

    def process(self):
        for handler in self.handlers:
            if handler.will_handle():
                return handler.handle()
