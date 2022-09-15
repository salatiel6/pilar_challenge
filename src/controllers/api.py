from server import server
from flask_restx import Resource
from flask import request
from docs import vowel_count_model, sort_model, default_error_model
from .error_handlers import ErrorHandlers
from .validators import Validators

app, api = server.app, server.api
app.config["REST_MASK_SWAGGER"] = False
error_handlers = ErrorHandlers


@api.route("/vowel_count", doc={
    "description": "Receives a list of words and counts the vowels of each one"
})
@api.param("payload", "List of words", _in="body")
@api.expect(vowel_count_model)
class VowelCount(Resource):
    @staticmethod
    @api.response(400, "BAD REQUEST", default_error_model)
    def post():
        request_data = request.json
        route = request.path

        validators = Validators(request_data)

        validators.validate_body_keys(route)
        validators.validate_key_values_types(route)
        validators.validate_words_list()

        return "passed"


@api.route("/sort", doc={
    "description": "Receives a list of words and order it according to "
                   "the order option"
})
@api.param("payload", "List of words and order option (asc or desc)",
           _in="body")
@api.expect(sort_model)
class Sort(Resource):
    @staticmethod
    def post():
        request_data = request.json
        route = request.path

        validators = Validators(request_data)

        validators.validate_body_keys(route)
        validators.validate_key_values_types(route)
        validators.validate_words_list()
        validators.validate_order_value()

        return "passed"
