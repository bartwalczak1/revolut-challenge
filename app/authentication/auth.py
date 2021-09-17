from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

USER_DATA = {"admin": "pass"}

@auth.verify_password
def verify(username, password) -> bool:
    """
    Basic auth helper function

    :param username: user name
    :param password: user password
    :return:
    """
    if not (username and password):
        return False

    return USER_DATA.get(username) == password
