## Analysis of Server Log Files

### Introduction
The Pandas library was employed to analyze server log files and observations of traffic data were plotted.

### Usage
The server.log and map.csv files are passed to the log_to_pandas.py module from main.py. The log file is parsed using regular expressions. Data mapping ip addresses to geographic locations, located in map.csv, were extracted and combined with log data and collected into a DataFrame. Subsequent data analysis on the respective DataFrame is carried out in main.py and includes observations of occurrences of ip addresses, and server traffic as a function of day and hour.

### Sample Results
A preview of the server log data is presented in Table-1. Server traffic as a function of daytime hour is illustrated below as both histogram and bar chart.


<div align="center">Table 1: Server Traffic DataFrame Preview</div>
<center>
<table border="1" class="dataframe">
<thead>
  <tr style="text-align: center;">
    <th></th>
    <th>IP Address</th>
    <th>Host</th>
    <th>Latitude</th>
    <th>Longitude</th>
    <th>Date</th>
    <th>Time</th>
    <th>Timezone</th>
  </tr>
</thead>
<tbody>
  <tr>
    <th>0</th>
    <td>61.245.171.187</td>
    <td>unknown</td>
    <td>6.9355</td>
    <td>79.8487</td>
    <td>01/May/2020</td>
    <td>00:06:42</td>
    <td>-0700</td>
  </tr>
  <tr>
    <th>1</th>
    <td>61.245.171.187</td>
    <td>unknown</td>
    <td>6.9355</td>
    <td>79.8487</td>
    <td>01/May/2020</td>
    <td>00:07:01</td>
    <td>-0700</td>
  </tr>
  <tr>
    <th>2</th>
    <td>45.152.32.204</td>
    <td>unknown</td>
    <td>52.3740</td>
    <td>4.8897</td>
    <td>01/May/2020</td>
    <td>00:14:54</td>
    <td>-0700</td>
  </tr>
  <tr>
    <th>3</th>
    <td>45.152.32.204</td>
    <td>unknown</td>
    <td>52.3740</td>
    <td>4.8897</td>
    <td>01/May/2020</td>
    <td>00:14:54</td>
    <td>-0700</td>
  </tr>
  <tr>
    <th>4</th>
    <td>45.152.32.204</td>
    <td>unknown</td>
    <td>52.3740</td>
    <td>4.8897</td>
    <td>01/May/2020</td>
    <td>00:14:55</td>
    <td>-0700</td>
  </tr>
</tbody>
</table>
</center>
<br>

<p align="center">
  <img src="/images/hist.png" alt="Histogram" style="height:auto; width:400px;"/>
  <div align="center">Figure 1: Histogram Representation</div>
</p>
<br>

<p align="center">
  <img src="/images/bar.png" alt="Barchart" style="height:auto; width:400px;"/>
  <div align="center">Figure 2: Bar Chart Representation</div>

### Next Steps
Future work will include consuming an API to gain insight on the global location associated to IP addresses recorded in the log file and chart this data on a map.   
