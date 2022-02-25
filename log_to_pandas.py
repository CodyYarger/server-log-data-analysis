"""
Module for log-file to pandas objects functions
"""

import numpy as np
import pandas as pd
import re


def get_log_data_list(file):
    """
        reads log files and stores lines in log_list
    """
    log_list = []

    # open file and define list data set to collect file lines
    with open(file, 'r') as logs:
        # append lines in log file to log_listead log data file
        for line in logs:
            log_list.append(line)
    return log_list


def get_addr_map_df(file):
    """
        converts map csv file to pandas df object
    """
    addr_map = pd.read_csv(file)
    return addr_map


def log_to_frame(log_list, df_map):

    # empty dataframe
    cols = ['ip', 'host', 'latitude', 'longitude', 'date', 'time', 'timezone']
    log_info = pd.DataFrame(columns=cols)

    # regex for ip  and timestamp
    reg_ip = r'(\d+[.]\d+[.]\d+[.]\d+)'
    reg_timestamp = r'\[(\d+\/\w+\/\d+):(\d+:\d+:\d+).(-\d+)]'

    for index, row in enumerate(log_list):
        # ip address = first instance of ip_reg found in string
        ipaddr = re.search(reg_ip, row).group()
        # print("This is the ip address")
        # print(ipaddr)

        # get time stamp
        date, time, timezone = re.search(reg_timestamp, log_list[index]).groups()

        # get series for ipaddr and convert to list
        try:
            map = (df_map.loc[df_map['ip'] == ipaddr]).values.tolist()
            # print(map_list)
        except KeyError:
            print("No key in dataframe")

        host, lat, long = map[0][1], map[0][2], map[0][3]

        d = {'ip': ipaddr, 'host': host, 'latitude': lat, 'longitude': long,
             'date': date, 'time': time, 'timezone': timezone}

        seriestest = pd.Series(
            data=d, index=['ip', 'host', 'latitude', 'longitude', 'date', 'time', 'timezone'])

        ser_final = pd.Series(data=d, index=['ip',
                                             'host',
                                             'latitude',
                                             'longitude',
                                             'date',
                                             'time',
                                             'timezone'])

        log_info = log_info.append(ser_final, ignore_index=True)
    print(log_info)
