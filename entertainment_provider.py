import abc


class EntertainmentProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_entertainment(self):
        pass
