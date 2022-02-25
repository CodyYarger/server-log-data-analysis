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
import os
import log_to_pandas as lp


def main():

    # current working directory and log file to process
    path = os.getcwd()
    f_log = 'small.log'
    f_csv = 'addrs.csv'

    # get log list
    log_list = lp.get_log_data_list(path + '/' + f_log)
    # get address map datafram from csv file
    df_map = lp.get_addr_map_df(path + '/' + f_csv)

    # get dataframe of log file with mapped geo location
    df_lf = lp.log_to_frame(log_list, df_map)
    print(df_lf)


if __name__ == "__main__":
    main()
