from server import server
from flask_restx import Resource
from flask import request
from docs import vowel_count_model, sort_model

app, api = server.app, server.api
app.config["REST_MASK_SWAGGER"] = False


@api.route("/vowel_count", doc={
    "description": "Receives a list of words and counts the vowels of each one"
})
@api.param("payload", "List of words", _in="body")
@api.expect(vowel_count_model)
class VowelCount(Resource):
    @staticmethod
    def post():
        request_data = request.json

        return request_data


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

        return request_data