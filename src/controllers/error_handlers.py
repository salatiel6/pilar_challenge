from server import server
from docs import default_error_model
from exceptions import BodyKeysError, WordsListError, KeysValuesTypesError,\
    OrderValueError

api = server.api


class ErrorHandlers:
    @staticmethod
    @api.errorhandler(BodyKeysError)
    @api.marshal_with(default_error_model, code=400)
    def handle_body_error_exception(error):
        return {'message': error.message}, 400

    @staticmethod
    @api.errorhandler(WordsListError)
    @api.marshal_with(default_error_model, code=400)
    def handle_words_list_error_exception(error):
        return {'message': error.message}, 400

    @staticmethod
    @api.errorhandler(KeysValuesTypesError)
    @api.marshal_with(default_error_model, code=400)
    def handle_words_list_error_exception(error):
        return {'message': error.message}, 400

    @staticmethod
    @api.errorhandler(OrderValueError)
    @api.marshal_with(default_error_model, code=400)
    def handle_words_list_error_exception(error):
        return {'message': error.message}, 400
