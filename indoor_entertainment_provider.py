import time

from entertainment_provider import EntertainmentProvider
import json
import requests
from hashlib import sha256
from datetime import datetime

class IndoorEntertainmentProvider(EntertainmentProvider):

    def __init__(self, config):
        self.config = config

    def get_entertainment(self):

        try:
            base_url = self.config.get('activity').get('base_url')
            response = requests.get(base_url)
            response.raise_for_status()

            activity = json.loads(response.text)
            print(activity)
            return activity
        except requests.exceptions.RequestException as re:
            print(re)
            return None