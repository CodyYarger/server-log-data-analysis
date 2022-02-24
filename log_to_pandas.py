"""
Module for log-file to pandas objects functions
"""

import numpy as np
import pandas as pd
import re


def _get_log_data(file):
    """
        reads log files and stores lines in log_list
    """
    # open file and define list data set to collect file lines
    with open(file, 'r') as logs:
        log_list = []

        # append lines in log file to log_listead log data file
        for line in logs:
            log_list.append(line)

    return log_list


def log_engtry_to_series(file, line):
    """
        converts log entries to pandas series object
    """

    # get list of log file lines
    log_list = _get_log_data(file)

    # regex for ip addresses: series of digits "d" and character sets "[]""
    reg_ip = r'(\d+[.]\d+[.]\d+[.]\d+)'
    # ip address = first instance of ip_reg found in string
    ipaddr = re.search(reg_ip, first).groups()
    print(ipaddr)

    # regex for time stamp
    reg_timestamp = r'\[(\d+\/\w+\/\d+):(\d+:\d+:\d+).(-\d+)]'
    date, time, timezone = re.search(reg_timestamp, first).groups()
    print(f'date: {date}, time: {time}, timezone: {timezone}')

    # datafram index
    cols = ['ip', 'host', 'latitude', 'longitude', 'date', 'time', 'timezone']

    log_series = pd.series()
