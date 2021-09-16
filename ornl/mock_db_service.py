class MockDbService:
    """
    A class that imitates, very loosely, a database.

    ...

    Attributes
    ----------
    config : dict
        A dictionary containing all the config values.

    Methods
    -------
    connect():
        Connect to the fake db.
    close():
        Close the connection to the fake db.
    save_current_weather():
        Save the current weather to the db.
    save_current_activity():
        Save teh current activity to the db.

    """

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

    def save_current_activity(self, activity):
        self.__activity.append(activity)

