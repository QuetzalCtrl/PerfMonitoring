# PerfMonitoring
## A simple performance monitoring script written in python

Performance monitoring involves tracking and measuring various metrics of a system or application to ensure that it is functioning optimally and meeting the desired performance goals.

Here I used the `psutil` library to collect performance metrics such as CPU usage, memory usage, and disk usage at a specified interval. This script includes threshold values for CPU, memory, and disk usage, and it sends an alert if any of these thresholds are exceeded. For this example, I used the `smtplib` library in order to send an alert by email when the thresholds are exceeded.
