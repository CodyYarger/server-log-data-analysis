#!/usr/bin/python3
# Dev: Cody Yarger
# 02/23/2022

"""
This module uses the Pandas and NumPy libraries to analyze a log file contaning
server traffic. URLs are extracted from the file and patterns are identified
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import log_to_pandas as lp
from matplotlib.pyplot import hist
import numpy as np


def main():

    # current working directory and files to process
    path = os.getcwd()
    f_log = 'medium.log'
    # f_log = 'small.log'
    f_csv = 'addrs.csv'

    # Get dataframe of log file and geographic map =============================
    # get log list
    log_list = lp.get_log_data_list(path + '/' + f_log)

    # get address map datafram from csv file
    df_map = lp.get_addr_map_df(path + '/' + f_csv)

    # get dataframe of log file with mapped geo location
    df_logf = lp.log_to_frame(log_list, df_map)
    print(df_logf)

    # Data analysis block ======================================================
    # dataframe for occurence of ip address in descending order
    top = df_logf['ip'].value_counts(ascending=False).reset_index()
    top.set_axis(['ip', 'count'], axis=1, inplace=True)
    # print(top)

    # dataframe for busiest day for server
    top_day = df_logf['date'].value_counts(ascending=False).reset_index()
    top_day.set_axis(['date', 'count'], axis=1, inplace=True)
    # print(top_day)

    # dataframe for hours of day
    top_hour = df_logf['time'].copy().to_frame()

    # slice hour off time stamp
    top_hour['time'] = top_hour['time'].str[: 2].str.strip()

    # map string hours to 24 hour int values
    hour_map = {'00': 0, '01': 100, '02': 200, '03': 300, '04': 400, '05': 500, '06': 600, '07': 700,
                '08': 800, '09': 900, '10': 1000, '11': 1100, '12': 1200, '13': 1300, '14': 1400, '15': 1500,
                '16': 1600, '17': 1700, '18': 1800, '19': 1900, '20': 2000, '21': 2100, '22': 2200, '23': 2300
                }

    # replace string hour data with integer hour data using map
    top_hour['time'] = top_hour['time'].map(hour_map)

    # Histogram for occurance of server traffic ================================
    top_hour.hist(bins=24, grid=True, color="yellow", ec="black")
    plt.xticks(fontsize=10, rotation=45, )
    plt.yticks(fontsize=10)
    plt.xlabel('Hour', fontsize=10, fontweight="bold")
    plt.ylabel('Server Traffic', fontsize=10, fontweight="bold")
    plt.title('User Server Traffic Distribution', fontsize=14, fontweight="bold")
    # ==========================================================================

    # add count column sorted descending add new (reset) index and rename columns
    top_hour = top_hour['time'].value_counts(ascending=False).reset_index()
    top_hour.set_axis(['hour', 'count'], axis=1, inplace=True)

    print(top_hour.head())
    print(type(top_hour))

    # Bar Graph for Occurence of Server Traffic  ===============================
    top_hour.sort_values(by=['hour'], inplace=True)
    top_hour.plot(x='hour', y='count', kind='bar')
    plt.xticks(fontsize=10, rotation=45)
    plt.xlabel('Hour', fontsize=10, fontweight="bold")
    plt.ylabel('Server Traffic', fontsize=10, fontweight="bold")
    plt.title('User Traffic vs Hour of Day', fontsize=14, fontweight="bold")
    # ==========================================================================
    plt.show()


if __name__ == "__main__":
    main()
