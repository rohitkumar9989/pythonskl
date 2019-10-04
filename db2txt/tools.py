#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" a set of function to dump content
"""

import sys
import sqlite3
import os
from logger import LOGGER
from configuration import SQL_COMMAND


def write_to_txt(data, txt_filename):
    """[summary]

    Arguments:
        data {[type]} -- [description]
        txt_filename {[type]} -- [description]
    """
    try:
        with open(txt_filename, "a") as f:
            f.write(data)
    except IOError:
        LOGGER.error("Could not write in file: {}".format(txt_filename))
        sys.exit("Problem to write in file.")


def read_db(db_name):
    """[summary]

    Arguments:
        db_name {[type]} -- [description]
    """
    conn = sqlite3.connect(db_name)
    result = conn.execute(SQL_COMMAND).fetchall()
    conn.close()
    return result


def convert_lt_2_string(list_of_tuples):
    """[summary]

    Arguments:
        list_of_tuples {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    output = "".join(str(list_of_tuples).strip('[]'))
    return output


def main(argv):
    """[summary]

    Arguments:
        argv {[type]} -- [description]
    """
    LOGGER.info(len(argv))
    if len(argv) != 3:
        sys.exit("Wrong list of arguments.")

    db_name = argv[1]
    txt_filename = argv[2]
    if not os.path.exists(db_name):
        LOGGER.error("db file {} doesn't exist.".format(db_name))
        sys.exit("db file {} doesn't exist.".format(db_name))

    if os.path.exists(txt_filename):
        LOGGER.info("txt file {} already exists.".format(txt_filename))

    db_output_nonstring = read_db(db_name)
    db_output = convert_lt_2_string(db_output_nonstring)
    write_to_txt(db_output, txt_filename)


if __name__ == "__main__":
    main(sys.argv)
