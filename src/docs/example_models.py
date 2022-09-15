from flask_restx import fields
from server import server

vowel_count_model = server.api.model(
    "vowel_count_model", {
        "words": fields.List(
            fields.String(),
            required=True,
            default=["batman", "robin"]
        )
    }
)

sort_model = server.api.model(
    "sort_model", {
        "words": fields.List(
            fields.String(),
            required=True,
            default=["batman", "robin"]
        ),
        "order": fields.String(required=True, default="asc")
    }
)
