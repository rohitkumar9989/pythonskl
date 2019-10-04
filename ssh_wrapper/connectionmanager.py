#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""[summary]"""
import os
import stat
import errno
import paramiko
from logger import LOGGER


class ConnectionManager():
    """[summary]"""

    def __init__(self, ip, ssh_user, ssh_password, ssh_port):
        """[summary]

        Arguments:
            ip {[type]} -- [description]
            ssh_user {[type]} -- [description]
            ssh_password {[type]} -- [description]
            ssh_port {[type]} -- [description]
        """
        self.ip_address = ip
        self.ssh_user = ssh_user
        self.ssh_password = ssh_password
        self.ssh_port = ssh_port

        try:
            LOGGER.info("creating(and connecting to) transport for {}@{}:{} with password {}.".format(
                self.ssh_user, self.ip_address, self.ssh_port, self.ssh_password))
            self.transport = paramiko.Transport(self.ip_address)
            self.transport.connect(username=self.ssh_user, password=self.ssh_password)
        except Exception as exception:
            LOGGER.error("Can't create a transport")
            LOGGER.error(exception)

        try:
            LOGGER.info("creating sftp for {}@{}:{} with password {}.".format(self.ssh_user, self.ip_address,
                                                                              self.ssh_port, self.ssh_password))
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        except Exception as exception:
            LOGGER.error("Can't create a ftp client")
            LOGGER.error(exception)

        try:
            LOGGER.info("ssh client is connecting to {}@{}:{} with password {}.".format(
                self.ssh_user, self.ip_address, self.ssh_port, self.ssh_password))
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(MissingHostKeyPolicy())
            self.ssh_client.load_system_host_keys()
            self.ssh_client.connect(self.ip_address,
                                    port=self.ssh_port,
                                    username=self.ssh_user,
                                    password=self.ssh_password)
        except Exception as exception:
            LOGGER.error("Can't create a ssh client")
            LOGGER.error(exception)

    def is_connection_open(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        if not self.transport.is_active() or not self.transport:
            return False
        try:
            self.transport.send_ignore()
        except Exception as exception:
            LOGGER.error("Transport is not active: {}.".format(exception))
            return False
        return True

    def run_command(self, command):
        """[summary]

        Arguments:
            command {[type]} -- [description]

        Keyword Arguments:
            timeout {int} -- [description] (default: {0})
            expected_return_code {int} -- [description] (default: {0})

        Returns:
            [type] -- [description]
        """
        LOGGER.info("Running command: {}.".format(command))
        try:
            # # good in case if there was a target reset between commands
            # if not self.is_connection_open():
            #     self.ssh_client.connect(self.ip_address, port=self.ssh_port,
            #                    username=self.ssh_user, password=self.ssh_password)
            stdin, stdout, stderr = self.ssh_client.exec_command(command)  # pylint: disable=unused-variable
            error_result = stderr.read()
            if error_result != b'':
                LOGGER.error("Command {} failed!".format(command))
                LOGGER.error(error_result)
                return False
            LOGGER.info(stdout.read())
        except Exception as exception:
            LOGGER.error("Command failed: {}.".format(command))
            LOGGER.error(exception)
            return False
        return True

    def copy_file_to_target(self, local_file_name, remote_target_location):
        """[summary]

        Arguments:
            local_file_name {[type]} -- [description]
            remote_target_location {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        try:
            LOGGER.info("copying {} to target {}".format(local_file_name, remote_target_location))
            self.sftp.put(local_file_name, remote_target_location)
        except Exception as exception:
            LOGGER.error("Cannot copy files to target")
            LOGGER.error(exception)
            return False
        return True

    def copy_file_from_target(self, file_name, target_location):
        """[summary]

        Arguments:
            file_name {[type]} -- [description]
            target_location {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        try:
            LOGGER.info("copying from target {} to {}".format(file_name, target_location))
            self.sftp.get(file_name, target_location)
        except Exception as exception:
            LOGGER.error("Cannot copy files from target")
            LOGGER.error(exception)
            return False
        return True

    def copy_dir_from_target(self, remote_dir, local_dir):
        """[summary]

        Arguments:
            remote_dir {[type]} -- [description]
            local_dir {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        try:
            LOGGER.info("copying directory from target {} to {}".format(remote_dir, local_dir))

            if not self.exists_remote(remote_dir):
                LOGGER.info("Remote directory doesn't exist {} ".format(remote_dir))
                return False

            for file_entry in self.sftp.listdir(remote_dir):
                LOGGER.info(file_entry)
                if stat.S_ISDIR(self.sftp.stat(remote_dir + file_entry).st_mode):
                    self.copy_dir_from_target(remote_dir + file_entry + '/',
                                              os.path.join(local_dir, file_entry))  # recursive copying
                else:
                    if not os.path.isfile(os.path.join(local_dir, file_entry)):
                        self.sftp.get(remote_dir + file_entry, os.path.join(local_dir, file_entry))
        except Exception as exception:
            LOGGER.error("Cannot copy files from target")
            LOGGER.error(exception)
            return False
        return True

    def exists_remote(self, path):
        """[summary]

        Arguments:
            path {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        try:
            self.sftp.stat(path)
        except IOError as exception:
            if exception.errno == errno.ENOENT:
                return False
            raise
        else:
            return True

    def __del__(self):
        """[summary]
        """
        self.ssh_client.close()
        self.transport.close()
        self.sftp.close()
        self.ip_address = None
        self.ssh_user = None
        self.ssh_port = None
        self.transport = None


class MissingHostKeyPolicy(paramiko.client.MissingHostKeyPolicy):
    """[summary] policy to use when server hostname is not in the system host keys or the application’s keys

    Arguments:
        paramiko {[type]} -- [description]
    """

    def missing_host_key(self, client, hostname, key):
        """[summary] accept every key

        Arguments:
            client {[type]} -- [description]
            hostname {[type]} -- [description]
            key {[type]} -- [description]
        """
        pass  # pylint: disable=unnecessary-pass
