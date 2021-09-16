from copy import copy


class LoggingService:
    """
    A class to perform logging.

    ...

    Attributes
    ----------
    config : dict
        A dictionary containing all the config values.

    Methods
    -------
    log_info(msg_text=""):
        Logs info messages.
    log_warn(msg_text=""):
        Logs warning messages.
    log_error(msg_text=""):
        Logs error messages.
    """

    __log_msgs = {
        'error': [],
        'info': [],
        'warn': []
    }

    def __init__(self, config):
        self.config = config;

    def log_info(self, msg_text):
        """
        Logs info messages.

        Parameters
        ----------
        msg_text : str
            The text of the message to log

        Returns
        -------
        None
        """
        message = {
            'msg_text': msg_text,
            'msg_date': 'PUT DATE HERE'
        }
        print('INFO: {}'.format(message))
        self.__log_msgs.get('info').append(message)

    def log_warn(self, msg_text):
        """
        Logs warning messages.

        Parameters
        ----------
        msg_text : str
            The text of the message to log

        Returns
        -------
        None
        """
        message = {
            'msg_text': msg_text,
            'msg_date': 'PUT DATE HERE'
        }
        print('WARNING: {}'.format(message))
        self.__log_msgs.get('warn').append(message)

    def log_error(self, msg_text, exception=None):
        """
        Logs error messages.

        Parameters
        ----------
        msg_text : str
            The text of the message to log

        Returns
        -------
        None
        """
        message = {
            'msg_text': msg_text,
            'msg_date': 'PUT DATE HERE'
        }

        if exception:
            message['exception'] = str(exception)

        print('ERROR: {}'.format(message))
        self.__log_msgs.get('error').append(message)
