"""
Module for log-file to pandas objects functions
"""

# pylint: disable=R0914
import re
import pandas as pd


def get_log_data_list(file):
    """
        reads log files and stores lines in log_list
    """
    log_list = []

    # open file and define list data set to collect file lines
    with open(file, 'r', encoding="utf-8") as logs:
        # append lines in log file to log_listead log data file
        for line in logs:
            log_list.append(line)
    return log_list


def get_addr_map_df(file):
    """
        converts map csv file to pandas df object. used by log_to_frame to map
        geo location to respective series
    """
    addr_map = pd.read_csv(file)
    return addr_map


def log_to_frame(log_list, df_map):
    """
        builds dataframe object from log file list and csv map of geo locations
    """
    # empty dataframe
    cols = ['ip', 'host', 'latitude', 'longitude', 'date', 'time', 'timezone']
    log_df = pd.DataFrame(columns=cols)

    # regex for ip and timestamp
    reg_ip = r'(\d+[.]\d+[.]\d+[.]\d+)'
    reg_timestamp = r'\[(\d+\/\w+\/\d+):(\d+:\d+:\d+).(-\d+)]'

    for index, row in enumerate(log_list):
        # ip address = first instance of ip_reg found in string
        ipaddr = re.search(reg_ip, row).group()

        # get time stamp
        date, time, timezone = re.search(reg_timestamp, log_list[index]).groups()

        # get series for ipaddr and convert to list
        try:
            maper = (df_map.loc[df_map['ip'] == ipaddr]).values.tolist()
        except KeyError:
            print("No key in dataframe")

        # unpack mapped data
        host, lat, long = maper[0][1], maper[0][2], maper[0][3]

        # axis map
        axis_map = {'ip': ipaddr,
                    'host': host,
                    'latitude': lat,
                    'longitude': long,
                    'date': date,
                    'time': time,
                    'timezone': timezone}

        # create series for row and map data
        ser_final = pd.Series(data=axis_map, index=['ip',
                                                    'host',
                                                    'latitude',
                                                    'longitude',
                                                    'date',
                                                    'time',
                                                    'timezone'])

        # append series to dataframe
        log_df = log_df.append(ser_final, ignore_index=True)

    return log_df
