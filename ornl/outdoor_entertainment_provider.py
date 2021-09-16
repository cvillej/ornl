from entertainment_provider import EntertainmentProvider

from random import randrange


class OutdoorEntertainmentProvider(EntertainmentProvider):
    """
    This class will provide an outdoor activity selected randomly from a list.

    ...

    Attributes
    ----------
    outdoor_activities : list
        A list of possible outdoor activities.

    Methods
    -------
    get_entertainment():
        Returns a random outdoor activity string.
    """

    outdoor_activities = [
        'Go for a run.',
        'Walk the dog.',
        'Mow the lawn.',
        'Heard the sheep.'
    ]

    def get_entertainment(self):
        """
        Select an outdoor activity randomly from a list.

        Returns
        -------
        str
            A sentence describing an outdoor activity.
        """
        idx = randrange(len(self.outdoor_activities) - 1)
        return self.outdoor_activities[idx]
