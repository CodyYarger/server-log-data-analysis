# Analysis of Server Log Files

## Introduction
Server log files were processed using Pandas and server traffic data is plotted.

## Discussion and Results
The sample.log and map.csv files are consumed by the log_to_pandas.py module.
The sample log file was parsed using regular expressions and data mapping ip
addresses to geographic locations, located in map.csv, were combined with log data
and collected into a DataFrame. Subsequent data analysis on the respective DataFrame was carried out in main.py and includes observations of server traffic as a function of daytime hour. These data are represented as both histogram and bar charts.  

<div align="center">Chart 1: Histogram Representation</div>
<p align="center">
  <img src="/images/hist.png" alt="Histogram" style="height:auto; width:400px;"/>
</p>


<div align="center">Chart 2: Bar Plot Representation</div>
<p align="center">
  <img src="/images/funct_calls.png" alt="Barchart" style="height:auto; width:400px;"/>
</p>
