from indoor_entertainment_provider import IndoorEntertainmentProvider
from outdoor_entertainment_provider import OutdoorEntertainmentProvider
from constants import INDOOR_PROVIDER, OUTDOOR_PROVIDER



# TODO: choose different provider based on config.  Change provider if one is not working
# TODO: Draw ascii art and return it if the provider is not afailable
# TODO: Have file that indicates if internet is ON or OFF
# get random provider or best provider
# choose provider based off the weather.  if weather is bad, sit home and look at ascii art
# if weather provider is down aka (no internet), flip a coin

class EntertainmentFactory:
    """
    We will select the correct provider based on the current weather.
    If the weather is good, we will get fandgo movie times.  If the weather is bad, we will draw the user
    a picture that they can view at home and not get wet.
    NOTE: Providers will be lazy loaded since we may never need them all.
    """
    providers = {}

    def __init__(self, config):
        self.config = config

    def get_provider(self, is_weather_good):
        # If the weather is good, we will go out to see a movie!
        # If it is bad, we will stay home and look at a picture
        if is_weather_good:
            if not (OUTDOOR_PROVIDER in self.providers):
                self.providers[OUTDOOR_PROVIDER] = OutdoorEntertainmentProvider(self.config)
            entertainment_provider = self.providers[OUTDOOR_PROVIDER]

        else:
            if not (INDOOR_PROVIDER in self.providers):
                self.providers[INDOOR_PROVIDER] = IndoorEntertainmentProvider(self.config)
            entertainment_provider = self.providers[INDOOR_PROVIDER]

        return entertainment_provider
