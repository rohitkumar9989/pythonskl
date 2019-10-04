#! /usr/bin/python3
# Write module which read YAML format config file and create ONE
# config<filename> class which convert each YAML item to class attribute
# magically (smile)

import json
import os

from own_logger import logger

config_name = "../assets/json_reader.json"  # only for testing purposes


class jsonconfiguration():

    def __init__(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return "".join(str(attr) + str(getattr(self, attr)) + "\n" for attr in dir(self) if not attr.startswith('__'))


def read_json(configName):
    '''
    function to read yaml file.
    Returns - dict with the data that was read from yaml, if file exists
            - None if file doesn't exist
    '''
    if not (os.path.exists(configName)):
        logger.error(
            "No config was found. Recheck if it exists: {}".format(configName))
        return None

    with open(configName, 'r') as configuration:
        conf = json.load(configuration)

    config = jsonconfiguration(conf)
    return config


def main():
    logger.info("Json reader.")
    conf = read_json(config_name)
    logger.info("Printing json configuration.")
    logger.info(conf)


if __name__ == "__main__":
    main()
