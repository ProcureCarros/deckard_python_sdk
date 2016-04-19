
import jwt

'''

 Class Base Client for the SDK
 this autenticates all requests and construct
 base api based ont eh definition on server



'''

## TODO: Make Client class work correctly
class Client(object):

    def discover(self, api_version, api_name, client_id = None, client_token = None):
        discoverInstance = self.__new__()

    def query(self, api_method, params):
        self._query(self.api_config.endpoint, api_method.rmethod, api_method.http_method, params)


    def _query(self, endpoint, method, http_method, params):
        return False

    def _sign(self):
        return ''

    def _e(self):
        encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')

    def _d(self, token):
        jwt.decode(token, 'secret', algorithms=['HS256'])




class ApiMethod(object):

    rmethod = ''
    http_method = ''


