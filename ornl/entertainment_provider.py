from abc import ABCMeta, abstractmethod


class EntertainmentProvider(metaclass=ABCMeta):
    """
    An Abstract Base Classes defining the functions needed for implementing classes.

    Methods
    -------
    get_entertainment(msg_text=""):
        Logs info messages.
    """

    @abstractmethod
    def get_entertainment(self):
        """
        Get and return an indoor or outdoor activity string.

        Returns
        -------
        str
            An indoor or outdoor activity.
        """
        pass
