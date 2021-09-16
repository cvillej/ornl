from entertainment_provider import EntertainmentProvider
import json
import requests


class IndoorEntertainmentProvider(EntertainmentProvider):
    """
    This class supports calling a REST API to retrieve indoor activity strings.

    ...

    Attributes
    ----------
    config : dict
        A dictionary containing all the config values.

    Methods
    -------
    get_entertainment():
        Calls a REST endpoint and return the activity or None.
    """

    def __init__(self, config):
        """
        Parameters
        ----------
        config : dict
            The configuration for the application
        """

        self.config = config

    def get_entertainment(self):
        """
        Calls a REST API to retrieve indoor activity strings

        Returns
        -------
        activity : str
            An indoor activity string.
        """
        try:
            base_url = self.config.get('activity').get('base_url')
            response = requests.get(base_url)
            response.raise_for_status()

            activity = json.loads(response.text)

            return activity
        except requests.exceptions.RequestException as re:
            print(re)
            return None
