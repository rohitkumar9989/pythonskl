#! /usr/bin/python3
# Write module which read YAML format config file and create ONE
# config<filename> class which convert each YAML item to class attribute
# magically (smile)

import os
import yaml
import pprint

config_name = "../assets/yaml_reader.yml"

class yamlconfiguration():
    '''ideal solution'''

    def __init__(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return "".join(str(attr) + str(getattr(self, attr)) +
                       "\n" for attr in dir(self) if not attr.startswith('__'))


def read_yaml(configName):
    '''
    function to read yaml file.
    Returns - dict with the data that was read from yaml, if file exists
            - None if file doesn't exist
    '''
    if not (os.path.exists(configName)):
        print("No config was found. Recheck if it exists: {}".format(configName))
        return None

    with open(configName, 'r') as configuration:
        conf = yaml.safe_load(configuration)

    configurationMap = yamlconfiguration(conf)
    return configurationMap


def main():
    print("just reading/printing input data in yaml reader.")
    configurationMap = read_yaml(config_name)
    
    print("class with dict solution.")
    confi = yamlconfiguration(configurationMap)
    print(confi)

if __name__ == "__main__":
    main()
