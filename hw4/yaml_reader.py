#! /usr/bin/python3
import os
import yaml
import pprint

config_name = "yaml_reader.yml"
#Write module which read YAML format config file and create ONE config<filename> class which convert each YAML item to class attribute magically (smile)

class Configuration():
    classes= []
    def __init__(self,yaml_data):
        [self.classes.append({key:value}) for key,value in configurationMap.items()]
            

    def __repr__(self):
        return "".join(str(value.keys()) + str(value.values()) + "\n" for value in (self.classes))

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
    print(type(conf))
    return conf


configurationMap = read_yaml(config_name)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(configurationMap)
#or
for key,value in configurationMap.items():
    print("{} {}".format(key,value))

confi = Configuration(configurationMap)
print(confi)