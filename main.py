#!/usr/bin/python3
# Dev: Cody Yarger
# 02/23/2022

"""
This module uses the Pandas and NumPy libraries to analyze a log file contaning
server traffic. URLs are extracted from the file and patterns are identified
"""

import os
import log_to_pandas as lp
import matplotlib.pyplot as plt


def main():

    # current working directory and files to process
    path = os.getcwd()
    f_log = 'small.log'
    f_csv = 'addrs.csv'

    # get log list
    log_list = lp.get_log_data_list(path + '/' + f_log)

    # get address map datafram from csv file
    df_map = lp.get_addr_map_df(path + '/' + f_csv)

    # get dataframe of log file with mapped geo location
    df_logf = lp.log_to_frame(log_list, df_map)
    print(df_logf)

    # dataframe for occurence of ip address in descending order
    top = df_logf['ip'].value_counts(ascending=False).reset_index()
    top.set_axis(['ip', 'count'], axis=1, inplace=True)
    print(top)
    print()

    # dataframe for occurence of time in descending order
    top_hour = df_logf['time'].value_counts(ascending=False).reset_index()
    top_hour.set_axis(['hour', 'count'], axis=1, inplace=True)
    print(top_hour)

    top_hour.plot.hist()


if __name__ == "__main__":
    main()
