# Analysis of Server Log Files

## Introduction
Server log files were analyzed and plotted using Pandas.

## Discussion and Results
The sample.log and map.csv files are consumed by the log_to_pandas.py module. The sample log file was parsed using regular expressions. Data mapping ip addresses to geographic locations, located in map.csv, were extracted and combined with log data and collected into a DataFrame. Subsequent data analysis on the respective DataFrame was carried out in main.py and includes observations of server traffic as a function of daytime hour. These data are represented as both histogram and bar charts, illustrated below.

<p align="center">
  <div align="center">Table 1: Server Traffic DataFrame Head</div>
  <table border="1" class="dataframe" align="center">
    <thead>
      <tr style="text-align: right;">
        <th></th>
        <th>ip</th>
        <th>host</th>
        <th>latitude</th>
        <th>longitude</th>
        <th>date</th>
        <th>time</th>
        <th>timezone</th>
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
</p>
<br>

<p align="center">
  <img src="/images/hist.png" alt="Histogram" style="height:auto; width:400px;"/>
  <div align="center">Figure 1: Histogram Representation</div>
</p>
<br>

<p align="center">
  <img src="/images/bar.png" alt="Barchart" style="height:auto; width:400px;"/>
  <div align="center">Figure 2: Bar Chart Representation</div>
</p>
