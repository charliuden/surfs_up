# Surfs Up

Hawaii surf weather analysis using jupyter notebook and visual studio code.

## Overview of the analysis

The goal of this analysis is to investigate weather data in Oahu with the goal of opening a surf and ice cream shop there. The weather data is stored in an SQLite database, hawaii.sqlite. This analysis looks at precipitation and temperature data over the course of the year 2016. The Flask Python module was used to display the results in a URL (code is found in app.py). 

In another script, SurfsUp_Challenge.ipynb, temperature data for the months of June and December are also looked at.  

## Results

![ScreenShot_juneTemps.png](https://github.com/charliuden/Surfs-Up/blob/main/Resources/ScreenShot_juneTemps.png)

![ScreenShot_decemberTemps.png](https://github.com/charliuden/Surfs-Up/blob/main/Resources/ScreenShot_decemberTemps.png)

* The mean temperature in December is just four degrees cooler than in June.
* The maximum temperature in December (83°F) is also not much cooler than June's maximum temperature (85°F) - just two degrees cooler. 
* However, December in Oahu can see chilly days -much chillier than in June. The coolest day in December was 56°F, while June's coolest day is 64°F. 

## Summary: 

Average temperatures during an Oahu December do not differ too much from June temperatures. In fact, there is a lot of overlap. However, some days in December can drop to temperatures below 60°F. If December is too chilly, the surf and ice cream shop may not do well during this month.

* How often do temperatures drop during December and is this something that I should be worried about? The standard deviation indicates that most of the data is within 3.7°F, so it is likely that these colder December days are infrequent. However, to get a clearer answer to this question, I would write a query to find the total number of December days that drop below 60°F: 

session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date) == 12).filter(Measurement.tobs =< 60).all()

* Is climate change something to consider? Are these colder days in December increasing over time? To answer this question, I would write a query to find the number of cold days (below 60°F) for every December. 

