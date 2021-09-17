import logging
from http import HTTPStatus

from app.parser.parser import DataParser
from app.authentication.auth import auth
from flask import abort, jsonify, request
from flask_restful import Resource


PARSE_ENDPOINT = "/api/parse"
logger = logging.getLogger(__name__)


class DataParserResource(Resource):
    @auth.login_required
    def post(self):
        """
        Parser POST method
        Parse incoming data and nest on arbitrary
        number of keys
        """

        try:
            data = request.json
            keys = request.args.get("keys")
            parsed_keys = [key.strip().lower() for key in keys.split(",")]
            parser = DataParser(keys=parsed_keys, data=data)
            res = parser.parse_data()
            return jsonify(res)
        except Exception as e:
            abort(HTTPStatus.BAD_REQUEST, e)
