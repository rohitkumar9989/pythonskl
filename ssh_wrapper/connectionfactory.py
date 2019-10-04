#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""[summary]
"""

from configuration import IP, SSH_PASSWORD, SSH_USER, SSH_PORT
from connectionmanager import ConnectionManager
from logger import LOGGER


class ConnectionFactory:
    "manage ssh, sftp conections"

    def __init__(self):
        """[summary]
        """
        try:
            self.connection = ConnectionManager(ip=IP, ssh_user=SSH_USER, ssh_password=SSH_PASSWORD, ssh_port=SSH_PORT)
        except Exception as exception:
            LOGGER.error("Problem to create a Connection.")
            LOGGER.error(exception)

    def get_connection(self):
        """[summary]

        Returns:Connection
            [type] -- [description]
        """
        return self.connection
