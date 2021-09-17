from mock_db_service import MockDbService
from mock_logging_service import LoggingService
from entertainment_factory import EntertainmentFactory
from weather_service import WeatherService


class EntertainmentService:
    """
    A class that will find entertainment.  It considers the city you live in and the weather there to make a judgement
    if you should do an indoor or outdoor activity.

    ...

    Attributes
    ----------
    config : dict
        A dictionary containing all the config values.

    Methods
    -------
    check_weather_is_good(city=""):
        Logs info messages.
    find_entertainment(city=""):
        Logs warning messages.
    log_error(msg_text=""):
        Logs error messages.
    """

    def __init__(self, config):
        """
        Parameters
        ----------
        config : dict
            The configuration for the application
        """

        self.logger = LoggingService(config)
        self.database = MockDbService(config)
        self.entertainment_factory = EntertainmentFactory(config)
        self.weather_service = WeatherService(config)

    def __enter__(self):
        try:
            self.database.connect()
        except ConnectionRefusedError as cre:
            self.logger.log_error('Unable to connect to database: {config}'.format(config=self.conf), exception=cre)

        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.database.close()

    def __check_weather_is_good(self, city):
        """
        Makes a very rude determination on of the weather is good.  If the weather description has the word 'rain'
        anywhere it is considered BAD weather.  Otherwise, it is considered GOOD weather.

        Parameters
        ----------
        city : str
            The city to check the weather in

        Returns
        -------
        boolean
            Is the weather good or bad
        """
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
        """
        Will find "entertainment" (A single text sentence suggesting an activity) based on the weather.  If the weather
        is good it will provide outdoor activities.  If it is bad, it will return an indoor activity.  It will
        also save the current activity and weather to the database.


        Parameters
        ----------
        city : str
            The city to check the weather in

        Returns
        -------
        activity : str
            A sentence describing an indoor or outdoor activity
        """
        self.logger.log_info('Get current weather...')
        is_good_weather = self.__check_weather_is_good(city)
        self.logger.log_info('Is the current weather in {} good? -- {}'.format(city, is_good_weather))
        self.database.save_current_weather(is_good_weather)

        entertainment_provider = self.entertainment_factory.get_provider(is_good_weather)
        self.logger.log_info('Because of the weather we are using an {}'.format(type(entertainment_provider)))

        activity = entertainment_provider.get_entertainment()

        self.database.save_current_activity(activity)

        return activity
