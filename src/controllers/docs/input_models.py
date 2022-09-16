from flask_restx import fields
from server import server

vowel_count_input_model = server.api.model(
    "vowel_count_input_model", {
        "words": fields.List(
            fields.String(),
            required=True,
            default=["batman", "robin", "joker"]
        )
    }
)

sort_input_model = server.api.model(
    "sort_input_model", {
        "words": fields.List(
            fields.String(),
            required=True,
            default=["batman", "robin", "joker"]
        ),
        "order": fields.String(required=True, default="asc")
    }
)
