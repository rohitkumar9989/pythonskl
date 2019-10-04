#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write multiprocessing module which convert all files in local directory (json, yaml) to list of
# python objects where each file type shall be handled in separately
# process and each file i separately thread. Please use multiprocessing
# POOL

import glob
import os
import sys
from multiprocessing import Pool

from json_reader import read_json
from own_logger import logger
from yaml_reader import read_yaml


def parseconfig(config_name):
    logger.info("Starting to parse: {}".format(config_name))

    if not (os.path.exists(config_name)):
        sys.exit(
            "No config was found. Recheck if it exists: {}".format(config_name))

    config = None
    if config_name.endswith(".yaml") or config_name.endswith(".yml"):
        config = read_yaml(config_name)
    elif config_name.endswith(".json"):
        config = read_json(config_name)
    return config


def read_all_from_directory(directory_name):
    if not (os.path.exists(directory_name)):
        sys.exit("No config was found. Recheck if it exists: {}".format(
            directory_name))
    abs_dir_name = os.path.abspath(directory_name)
    logger.info("Starting to look for configs in: {}".format(abs_dir_name))

    configurationFiles = glob.glob('{}/*'.format(abs_dir_name))
    logger.info(configurationFiles)
    return configurationFiles


def printallconfigs(directory_name):
    config_files = read_all_from_directory(directory_name)

    with Pool(8) as p:
        print(p.map(parseconfig, config_files))


def main():
    logger.info(parseconfig("../assets/json_reader.json"))
    read_all_from_directory('../assets/')
    printallconfigs('../assets/')


if __name__ == "__main__":
    main()
