from copy import copy


class MockDbService:

    __weather = []
    __activity = []

    def __init__(self, config):
        self.config = config

    def connect(self):
        # initialize the DB connection
        pass

    def close(self):
        # close the DB connection
        pass

    def save_current_weather(self, weather):
        self.__weather.append(weather)

    def save_current_activiy(self, activity):
        self.__activity.append(activity)

