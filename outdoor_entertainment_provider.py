from entertainment_provider import EntertainmentProvider

from random import randrange


class OutdoorEntertainmentProvider(EntertainmentProvider):
    outdoor_activities = [
        'Go for a run.',
        'Walk the dog.',
        'Mow the lawn.',
        'Heard the sheep.'
    ]

    def __init__(self, config):
        pass

    def get_entertainment(self):
        idx = randrange(len(self.outdoor_activities) - 1)
        return self.outdoor_activities[idx]
