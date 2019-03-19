#! /usr/bin/python3
# Write module which read YAML format config file and create ONE
# config<filename> class which convert each YAML item to class attribute
# magically (smile)

import os
import yaml

from own_logger import logger

config_name = "../assets/yaml_reader.yml"  # only for testing purposes


class yamlconfiguration():

    def __init__(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return "".join(str(attr) + str(getattr(self, attr)) + "\n" for attr in dir(self) if not attr.startswith('__'))


def read_yaml(configName):
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
        conf = yaml.safe_load(configuration)

    config = yamlconfiguration(conf)
    return config


def main():
    logger.info("Yaml reader module.")
    conf = read_yaml(config_name)
    logger.info("Printing yaml configuration.")
    logger.info(conf)


if __name__ == "__main__":
    main()
