import click
import json

from entertainment_service import EntertainmentService


@click.command()
@click.option('--city',
              prompt='Enter City',
              help='The city you are in',
              required=True,
              type=click.Choice(['London', 'New York', 'Sidney']))
@click.option('--username', prompt='Enter Username',  help='Your username (can be any string)', required=True)
@click.option('--config_file', default='config.json', help='File containing configuration in json format', required=True)
def provide_entertainment(city, username, config_file):
    """
    This is the entrypoint for the program.  It will leverage the EntertainmentService to find
    entertainment for you, despite the weather :)

    Parameters
    ----------
    city : str
        The name of the city you are interested in.  Valid options are: London, New York, Sidney
    username : str
        Any username string
    config_file : str
        the config file path.  NOTE: Local config path is supported
    """

    try:
        config = load_config_file(config_file)
    except FileNotFoundError:
        print('Configuration file: {} not found.  Exiting...'.format(config_file))
        quit()
    with EntertainmentService(config) as entertainment_service:
        entertainment_service.find_entertainment(city)


def load_config_file(config_file_path):
    """Load the json config file from disk"""
    with open(config_file_path, 'r') as config_data:
        config = json.load(config_data)
    return config


if __name__ == '__main__':
    provide_entertainment()
