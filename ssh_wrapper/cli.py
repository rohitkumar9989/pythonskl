#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""[summary]
"""

import os
import sys

import click  # pylint: disable=import-error
from connectionfactory import ConnectionFactory
from logger import LOGGER


@click.group()
def cli():
    """[summary]
    """
    LOGGER.info("{} {}".format(sys._getframe().f_code.co_name, locals()))


CONNECTION = ConnectionFactory().get_connection()


@cli.command('executeOnTarget')
@click.option('-what', help='what folder to list', nargs=1, required=True)
def execute_command(what):
    """[summary]

    Arguments:
        what {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    LOGGER.info("execute_command {}".format(what))
    try:
        if not CONNECTION.run_command(command=what):
            LOGGER.error("Command failed!")
            return False
    except Exception as exception:
        LOGGER.error("can't execute command on target")
        LOGGER.error(exception)
        return False
    return True


@cli.command('copy2target')
@click.option('-localfile', help='file to copy on target', nargs=1, required=True, type=click.Path(exists=True))
@click.option('-where', help='target location of file to copy on target', nargs=1, required=True, type=str)
def copy_file_to_target_cli(localfile, where):
    """[summary]

    Arguments:
        localfile {[type]} -- [description]
        where {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    LOGGER.info("copy_file_to_target_cli {} {}".format(localfile, where))
    try:
        if not CONNECTION.copy_file_to_target(local_file_name=localfile, remote_target_location=where):
            LOGGER.error("Command failed!")
            return False
    except Exception as exception:
        LOGGER.error("can't call copy file to target")
        LOGGER.error(exception)
        return False
    return True


@cli.command('copyFromTarget')
@click.option('-targetfile', help='file to copy from target', nargs=1, required=True)
@click.option('-where', help='target location of file to copy on local machine', nargs=1, required=True)
def copy_file_from_target_cli(targetfile, where):
    """[summary]

    Arguments:
        targetfile {[type]} -- [description]
        where {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    LOGGER.info("copy_file_from_target_cli {} {}".format(targetfile, where))
    try:
        if not CONNECTION.copy_file_from_target(file_name=targetfile, target_location=where):
            LOGGER.error("Command failed!")
            return False
    except Exception as exception:
        LOGGER.error("can't call copy file from target")
        LOGGER.error(exception)
        return False
    return True


@cli.command('copyDirFromTarget')
@click.option('-target_dir', help='dir to copy from target', nargs=1, required=True)
@click.option('-local_dir', help='dir on local machine', nargs=1, required=True)
def copy_dir_from_target_cli(target_dir, local_dir):
    """[summary]

    Arguments:
        target_dir {[type]} -- [description]
        local_dir {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    LOGGER.info("copy_dir_from_target_cli {} {}".format(target_dir, local_dir))
    if not os.path.exists(local_dir):
        os.mkdir(local_dir)
    try:
        if not CONNECTION.copy_dir_from_target(remote_dir=target_dir, local_dir=local_dir):
            LOGGER.error("Command failed!")
            return False
    except Exception as exception:
        LOGGER.error("can't call copy file from target")
        LOGGER.error(exception)
        return False
    return True


if __name__ == "__main__":
    cli()
