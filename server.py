import math
import decimal

from flask import Flask
from flask_cors import CORS
from flask_restful import (
    Api,
    Resource,
    abort,
    reqparse,
)

from db import (
    db,
    Triangulo,
)

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


def calc_triangulo(cateto_a, cateto_b):
    hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
    return round(hipotenusa, 2)


parser = reqparse.RequestParser()
parser.add_argument(
    "cateto_a",
    required=True,
    type=decimal.Decimal,
)
parser.add_argument(
    "cateto_b",
    required=True,
    type=decimal.Decimal,
)


def _to_json(triangulo):
    return {
        "id": triangulo.id,
        "cateto_a": str(triangulo.cateto_a),
        "cateto_b": str(triangulo.cateto_b),
        "hipotenusa": str(triangulo.hipotenusa),
    }


class PitagorasResource(Resource):
    """Pitagoras REST resource."""

    def get(self):
        return [_to_json(t) for t in Triangulo.select()]

    def post(self):
        args = parser.parse_args()
        if (args.get("cateto_a") or 0) <= 0:
            abort(400, message="cateto_a needs to be higher than 0")
        if (args.get("cateto_b") or 0) <= 0:
            abort(400, message="cateto_b needs to be higher than 0")
        t = Triangulo(cateto_a=args["cateto_a"], cateto_b=args["cateto_b"])
        t.hipotenusa = calc_triangulo(t.cateto_a, t.cateto_b)

        t.save()
        return _to_json(t), 201


api.add_resource(PitagorasResource, "/pitagoras")

if __name__ == "__main__":
    db.create_tables([Triangulo])
    app.run(debug=True)
