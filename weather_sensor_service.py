import json
import requests

from mock_logging_service import LoggingService

# https://openweathermap.org/current    API
class WeatherSensorService():
    # BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    # BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=7fc1fc145d4c4c82e328bf03292403df"
    # CITY = 'London'
    # API_KEY = '7fc1fc145d4c4c82e328bf03292403df'
    # API_KEY = '3828031312f5583804b0f1cec6e70092']

    def __init__(self, config):
        self.config = config
        self.logger = LoggingService()

        self.base_url = self.config.get('weather').get('base_url')
        self.query_string_template = '{city}&appid={api_key}'
        self.api_ky = self.config.get('weather').get('api_key')

    def get_weather(self, city):
        try:
            url = self.base_url + self.query_string_template.format(city=city, api_key=self.api_ky)
            response = requests.get(url)
            response.raise_for_status()
            return json.loads(response.text)
        except requests.exceptions.RequestException as re:
            self.logger.log_error(re)
            return None

