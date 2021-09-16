from copy import copy


class LoggingService:

    __log_msgs = {
        'error': [],
        'info': [],
        'warn': []
    }

    def log_info(self, msg_text):
        message = {
            'msg_text': msg_text,
            'msg_date': 'PUT DATE HERE'
        }
        print('INFO: {}'.format(message))
        self.__log_msgs.get('info').append(message)

    def log_warn(self, msg_text):
        message = {
            'msg_text': msg_text,
            'msg_date': 'PUT DATE HERE'
        }
        print('WARNING: {}'.format(message))
        self.__log_msgs.get('warn').append(message)

    def log_error(self, msg_text, exception=None):
        message = {
            'msg_text': msg_text,
            'msg_date': 'PUT DATE HERE'
        }

        if exception:
            message['exception'] = str(exception)

        print('ERROR: {}'.format(message))
        self.__log_msgs.get('error').append(message)

    def get_info_logs(self):
        return copy(self.__log_msgs.get('info'))

    def get_error_logs(self):
        return copy(self.__log_msgs.get('error'))

    def get_all_logs(self):
        return copy(self.__log_msgs)
