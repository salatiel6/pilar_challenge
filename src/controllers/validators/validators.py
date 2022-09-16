from controllers.exceptions import BodyKeysError, WordsListError, \
    KeysValuesTypesError, OrderValueError


class Validators:
    def __init__(self, request_data):
        self.request_data = request_data

    def validate_body_keys(self, route):
        key = "words"
        try:
            _ = self.request_data[key]
            if route == "/sort":
                key = "order"
                _ = self.request_data[key]
        except KeyError:
            raise BodyKeysError(key)

    def validate_key_values_types(self, route):
        words = self.request_data["words"]
        if not type(words) == list:
            raise KeysValuesTypesError("words")

        if route == "/sort":
            order = self.request_data["order"]
            if not type(order) == str:
                raise KeysValuesTypesError("order")

    def validate_words_list(self):
        words = self.request_data["words"]
        str_list = all(isinstance(item, str) for item in words)

        if not str_list or "" in words:
            raise WordsListError()

    def validate_order_value(self):
        order = self.request_data["order"]

        if order != "asc" and order != "desc":
            raise OrderValueError()
