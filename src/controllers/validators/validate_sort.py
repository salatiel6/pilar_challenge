from .validators import Validators


class ValidateSort:
    def __init__(self, request_data, route):
        self.request_data = request_data
        self.route = route

    def validate(self):
        validators = Validators(self.request_data)

        validators.validate_body_keys(self.route)
        validators.validate_key_values_types(self.route)
        validators.validate_words_list()
        validators.validate_order_value()
