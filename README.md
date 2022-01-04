# Surfing-and-Weather-Analysis

**Temperature Trends for Proposed Oahu Surf Shop**

**Project Overview**
The purpose of this project is to analyze the temperature trends in Oahu, Hawaii for a hypothetical client seeking to open a surf shop. Specifically, the temperature trends during the months of June and December are analyzed so that the client can make a more informed decision.

**Resources and Software**
Starting File: hawaii.sqlite
Python 3.10.0
psycopg2-binary
SQLAlchemy

**Results**
1. The average temperature in Oahu during December is only 3.9°F cooler than June.
2. The lowest temperature in December is 8°F colder than the lowest temperature in June.
3. There are 10.7% less data points in December than June.

**Below is a statistical summary for the month of June**

![June Temperature Statistics](https://user-images.githubusercontent.com/93059601/148138768-8f96871d-8039-4003-853b-37ac94a51272.PNG)










Below is a statistical summary for the month of December:

![December Temperature Statistics](https://user-images.githubusercontent.com/93059601/148138801-875277fa-6962-452f-b1ae-a5c050ee8e26.PNG)





**Summary**

Based on the results above, it can be expected that a surf shop in Oahu will have more customers in June than in December due to the slight decrease in average daily temperature.

It is important to have the most relevant results when conducting analysis on a potential business venture. For this reason, we carried out two additional queries for  June and December to obatin additional  weather data about precipitation for these periods. 

The query below will find precipitation scores in June:

session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 6).all()

The query below will find precipitation scores in December:

session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 12).all()

