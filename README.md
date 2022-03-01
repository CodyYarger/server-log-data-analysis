# Analysis of Server Log Files

## Introduction
Server log files were processed using Pandas and server traffic data is plotted.

## Discussion and Results
The sample.log and map.csv files are consumed by the log_to_pandas.py module.
The sample log file was parsed using regular expressions and data mapping ip
addresses to geographic locations, located in map.csv, were combined with log data
and collected into a DataFrame. Subsequent data analysis on the respective DataFrame was carried out in main.py and includes observations of server traffic as a function of daytime hour. These data are represented as both histogram and bar charts, illustrated below.  

<p align="center">
  <img src="/images/hist.png" alt="Histogram" style="height:auto; width:400px;"/>
</p>
<div align="center">Figure 1: Histogram Representation</div>


<p align="center">
  <img src="/images/bar.png" alt="Barchart" style="height:auto; width:400px;"/>
</p>
<div align="center">Figure 2: Bar Chart Representation</div>
