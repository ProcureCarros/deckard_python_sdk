from procurecarros_sdk.client import Client


class Integration(object):

    def __init__(self, client_id = None, access_token = None):
        self.client = Client.discover('v1', 'integration', client_id, access_token)

    def load_clients(self):
        ret = self.client.query("", "")
        return []

    def load_jobs(self):
        ret = self.client.query("", "")
        return []