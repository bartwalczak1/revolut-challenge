import base64
import json

from app.parser.parser import DataParser
from flask.testing import FlaskClient

from tests.data.sample_input import data

HTTP_AUTHORIZATION = "Basic " + base64.b64encode(b"admin:pass").decode()


def test_end_chat(client: FlaskClient):
    """
    Test POST end chat.
    :param client: Flask test client.
    """
    headers = {"Authorization": HTTP_AUTHORIZATION, "content-type": "application/json"}

    # bad request
    res = client.post("/api/parse", headers=headers)
    assert res.status_code == 400

    # unauthorized
    res = client.post("/api/parse")
    assert res.status_code == 401
    assert res.json == None

    # authorized
    res = client.post("/api/parse?keys=city", data=json.dumps(data), headers=headers)
    assert res.status_code == 200

    # authorized missing json
    headers = {"Authorization": HTTP_AUTHORIZATION}
    res = client.post("/api/parse?keys=city", headers=headers)
    assert res.status_code == 400


def test_nested_dicts():
    """
    Test inserting orphaned dict into nested dict
    """
    non_grouped_dict = {"amount": 100}
    keys = ["US", "USD", "Boston"]
    nested = {}
    DataParser._nest_dict(nested, keys, non_grouped_dict)
    assert nested == {"US": {"USD": {"Boston": [{"amount": 100}]}}}
