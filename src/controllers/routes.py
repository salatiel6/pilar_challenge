from server import server
from flask_restx import Resource
from flask import request
from git import Repo
from .docs import vowel_count_model, sort_model, default_error_model
from .handlers import ErrorHandlers, ProcessHandler
from .validators import ValidateVowelCount, ValidateSort

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

        validator = ValidateVowelCount(request_data, route)
        validator.validate()

        process_handler = ProcessHandler(request_data, route)
        vowel_count_result = process_handler.process()

        return vowel_count_result


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

        validate = ValidateSort(request_data, route)
        validate.validate()

        process_handler = ProcessHandler(request_data, route)
        sort_result = process_handler.process()

        return sort_result


@app.route("/deploy", methods=["POST"])
def deploy():
    if request.method == 'POST':
        repo = Repo('../')

        origin = repo.remotes.origin
        origin.pull()

        return 'Updated PythonAnywhere successfully', 200

    return 'Wrong event type', 400
