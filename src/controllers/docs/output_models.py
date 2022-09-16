from flask_restx import fields
from server import server

vowel_count_output_model = server.api.model(
    "vowel_count_output_model", {
        "batman": fields.Integer(default=2),
        "robin": fields.Integer(default=2),
        "joker": fields.Integer(default=2)
    }
)

sort_output_model = server.api.model(
    "sort_output_model", {
            "result": fields.List(
                        fields.String(),
                        required=True,
                        default=["word", "word", "word"]
                    )
    }
)
