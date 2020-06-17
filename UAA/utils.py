import requests, json, jwt
from requests.auth import HTTPBasicAuth

from UAA.settings import UAA_CLIENT_ID, UAA_CLIENT_SECRET, UAA_ISSUER_URI


class UAAAuth:
    @staticmethod
    def decode_token(token):
        return jwt.decode(token, verify=False)

    @staticmethod
    def authenticate(username, password):
        client_auth = HTTPBasicAuth(UAA_CLIENT_ID, UAA_CLIENT_SECRET)
        retval = requests.post(url=UAA_ISSUER_URI, headers={'accept': 'application/json'},
                               params={'username': username, 'password': password, 'grant_type': 'password',
                                       'client_id': UAA_CLIENT_ID}, auth=client_auth)
        return UAAAuth.decode_token(json.loads(retval.content.decode('utf-8'))['access_token'])


