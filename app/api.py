import logging
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from app.resources.parser_resource import DataParserResource, PARSE_ENDPOINT


def run_app():
    """
    Create and run app
    """
    # Configure loggging. Print all logs to stdout
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%d-%m %H:%M",
        stream=sys.stdout,
    )

    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    api.add_resource(DataParserResource, PARSE_ENDPOINT, f"{PARSE_ENDPOINT}/<keys>")

    return app


if __name__ == "__main__":
    app = run_app()
    app.run(host="0.0.0.0")
