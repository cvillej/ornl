import json
import requests

from mock_logging_service import LoggingService


class WeatherService:
    """
    A class to lookup weather, based on the city passed in.

    ...

    Attributes
    ----------
    config : dict
        A dictionary containing all the config values.
    logger : object
        A class that mocks logging capability
    base_url : str
        The base url for the weather rest endpoint
    query_string_template : str
        Appended to the base_url, it contains the query params required for the REST endpoint.
    api_ky : str
        The api key needed to access the REST endpoint

    Methods
    -------
    get_weather(city=""):
        Gets a weather report, in json format, for the city passed in.
    """

    def __init__(self, config):
        """
        Parameters
        ----------
        config : dict
            The configuration for the application
        """

        self.config = config
        self.logger = LoggingService(config)

        self.base_url = self.config.get('weather').get('base_url')
        self.query_string_template = '{city}&appid={api_key}'
        self.api_ky = self.config.get('weather').get('api_key')

    def get_weather(self, city):
        """
        Gets a weather report, in json format, for the city passed in.

        Parameters
        ----------
        city : str
            The city to query the endpoint by.

        Returns
        -------
        city_weather : dict || None
            The weather report for the city.
        """

        try:
            url = self.base_url + self.query_string_template.format(city=city, api_key=self.api_ky)
            response = requests.get(url)
            response.raise_for_status()

            city_weather = json.loads(response.text)

            return city_weather
        except requests.exceptions.RequestException as re:
            self.logger.log_error(re)
            return None

