
import jwt
import os
import json
from collections import namedtuple

'''

 Class Base Client for the SDK
 this autenticates all requests and construct
 base api based ont eh definition on server



'''

## TODO: Make Client class work correctly
class Client(object):

    def __init__(self, api_config = None):
        self.api_config = api_config
        self.client_config = {
            'server_uri': os.getenv('PROCURECARROS_API_SERVER', 'http://api.procurecarros.com/'),
            'autorizarion': True
        }

        self.credentials = {
            'client_id': '',
            'access_token': ''
        }


    def set_authorization(self, client_id, access_token):
        self.credentials['client_id'] = client_id
        self.credentials['access_token'] = access_token

    @staticmethod
    def discover(api_version, api_name, client_id = None, client_token = None):
        discoverInstance = Client()
        if client_id is not None and client_token is not None:
            discoverInstance.set_authorization(client_id, client_token)
        retorno_discovery = discoverInstance._query("discover", api_version+"/"+api_name, 'get', {})
        if retorno_discovery is None:
            raise Exception(">>api_manager: Cannot get API")
        elif retorno_discovery['errors'] is not None:
            raise Exception(">>api_manager: Error when getting the api: "+retorno_discovery["errors"])
        # TODO: fazer com que o retorno seja um objeto e depois carregar ele em uma instancia na qual irá retornar
        api_config = retorno_discovery["obj"]
        # api_config = Hashie::Mash.new retorno_discovery["obj"]
        # instance = self.new api_config
        # if !client_id.nil? && !client_token.nil?
        # instance.credentials(client_id, client_token)
        # end
        # return instance
        return instance

    def query(self, api_method, params):
        self._query(self.api_config.endpoint, api_method.rmethod, api_method.http_method, params)


    def _query(self, endpoint, method, http_method, params):
        return False

    def _sign(self):
        return ''

    def _e(self, payload):
        # payload == {'some': 'payload'}
        encoded = jwt.encode(payload, 'secret', algorithm='HS256')

    def _d(self, token):
        jwt.decode(token, 'secret', algorithms=['HS256'])

class ApiMethod(object):

    def __init__(self):
        self.endpoint = ''
        self.rmethod = ''
        self.http_method = ''


