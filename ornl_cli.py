import click
import json

from entertainment_service import EntertainmentService


@click.command()
@click.option('--city', prompt='Enter City', help='The city you are in', required=True)
@click.option('--username', prompt='Enter Username',  help='Your username (can be any string)', required=True)
@click.option('--config_file', default='config.json', help='File containing configuration in json format', required=True)
# def provide_entertainment(name, zip, config_file):
def provide_entertainment(city, username, config_file):
    """Simple program that greets NAME for a total of COUNT times."""

    config = load_config_file(config_file)
    with EntertainmentService(config) as entertainment_service:
        entertainment_service.find_entertainment(city)


def load_config_file(config_file_path):
    with open(config_file_path, 'r') as config_data:
        config = json.load(config_data)
    return config


if __name__ == '__main__':
    provide_entertainment()
