import requests


class SendRequest:
    def __init__(self):
        self.session = requests.Session()

    def all_send_request(self):
        self.session.request()
