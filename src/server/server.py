from flask import Flask
from flask_restx import Api


class Server:
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            default="Endpoints",
            default_label="from API",
            version="v0.7.3",
            title="Pilar Challenge API",
            doc="/docs"
        )

    @staticmethod
    def run(app):
        app.run(
            debug=True,
            host="0.0.0.0",
            port=4670
        )


server = Server()
