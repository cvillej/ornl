from mock_db_service import MockDbService
from mock_logging_service import LoggingService
from entertainment_factory import EntertainmentFactory
from weather_sensor_service import WeatherSensorService


class EntertainmentService:

    def __init__(self, config):
        self.logger = LoggingService()
        self.database = MockDbService(config)
        self.entertainment_factory = EntertainmentFactory(config)
        self.weather_service = WeatherSensorService(config)

    def __enter__(self):
        try:
            self.database.connect()
        except ConnectionRefusedError as cre:
            self.logger.log_error('Unable to connect to database: {config}'.format(config=self.conf), exception=cre)

        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.database.close()

    def check_weather_is_good(self, city):
        weather = self.weather_service.get_weather(city)
        if weather is None:
            self.logger.log_warn("Unable to get current weather for: {}".format(city))
            self.logger.log_warn("We will assume the weather is bad...")

            # The weather service failed.  We better default to bad weather
            return False

        # We only need the first item in the result array.  The other items
        weather_for_city = weather.get('weather')[0]
        self.logger.log_info('weather for city: ' + weather_for_city.get('description'))
        if 'rain' in weather_for_city.get('description').lower():
            self.logger.log_info('weather: {}'.format(weather_for_city))
            return False

        return True

    def find_entertainment(self, city):
        is_good_weather = self.check_weather_is_good(city)
        entertainment_provider = self.entertainment_factory.get_provider(is_good_weather)

        return entertainment_provider.get_entertainment()
