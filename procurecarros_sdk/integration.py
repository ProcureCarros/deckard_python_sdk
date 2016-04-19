from procurecarros_sdk.client import Client


class Integration(object):

    def __init__(self):
        self.client = Client()

    def load_clients(self):
        ret = self.client.query("")
        return []

    def load_jobs(self):
        ret = self.client.query("")
        return []