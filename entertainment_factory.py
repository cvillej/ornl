from indoor_entertainment_provider import IndoorEntertainmentProvider
from outdoor_entertainment_provider import OutdoorEntertainmentProvider
from constants import INDOOR_PROVIDER, OUTDOOR_PROVIDER


class EntertainmentFactory:
    """
    This factory class will provide an implementation to provide activities, either indoor or outdoor, based on
    weather conditions.

    ...

    Attributes
    ----------
    config : dict
        A dictionary containing all the config values.

    Methods
    -------
    get_provider(is_weather_good):
        Get an indoor or outdoor provider depending on weather.
    """

    providers = {}

    def __init__(self, config):
        """
        Parameters
        ----------
        config : dict
            The configuration for the application
        """

        self.config = config

    def get_provider(self, is_weather_good):
        """
        Get an indoor or outdoor entertainment provider.

        Parameters
        ----------
        is_weather_good : bool
            A flag indicating if the weather is good.

        Returns
        -------
        EntertainmentProvider
            Either an indoor or outdoor entertainment provider.
        """
        if is_weather_good:
            if not (OUTDOOR_PROVIDER in self.providers):
                self.providers[OUTDOOR_PROVIDER] = OutdoorEntertainmentProvider()
            entertainment_provider = self.providers[OUTDOOR_PROVIDER]

        else:
            if not (INDOOR_PROVIDER in self.providers):
                self.providers[INDOOR_PROVIDER] = IndoorEntertainmentProvider(self.config)
            entertainment_provider = self.providers[INDOOR_PROVIDER]

        return entertainment_provider
