#!/usr/bin/python3
# Dev: Cody Yarger
# 02/23/2022

"""
This module uses the Pandas and NumPy libraries to analyze a log file contaning
server traffic. URLs are extracted from the file and patterns are identified
"""

# import numpy as np
# import pandas as pd
# import re
import log_to_pandas as topan


def main():
    # open file and define list data set to collect file lines
    with open('small.log', 'r') as logs:
        log_list = []

        # read log data file
        for line in logs:
            log_list.append(line)

    first = log_list[0]
    print(first)

    # ---------------------------------------------------------------------------
    # get ip address and time stamp from log file.

    # # regex for ip addresses: series of digits "d" and character sets "[]""
    # reg_ip = r'(\d+[.]\d+[.]\d+[.]\d+)'
    # # ip address = first instance of ip_reg found in string
    # ipaddr = re.search(reg_ip, first).group(1)
    # print(ipaddr)
    #
    # # regex for time stamp
    # reg_timestamp = r'\[(\d+\/\w+\/\d+):(\d+:\d+:\d+).(-\d+)]'
    # date, time, timezone = re.search(reg_timestamp, first).groups()
    # # print(date)
    # print(f'date: {date}, time: {time}, timezone: {timezone}')

    # dataframe for map data in local file
    addr_map = pd.read_csv(
        '/home/cody/Desktop/PYTHON/Python_Projects/log_file_data_analysis/addrs.csv')
    print(addr_map)

    # dataframe for axis0 containing ipaddr
    df_new = addr_map[addr_map['ip'] == ipaddr]

    print(df_new)


if __name__ == "__main__":
    main()
