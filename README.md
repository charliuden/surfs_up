# Surfs Up

Hawaii surf weather analysis using jupyter notebook and visual studio code.

## Overview of the analysis

The goal of this analysis is to investigate weather data in Oahu with the goal of opening a surf and ice cream shop there. The weather data is stored in a SQLite database, hawaii.sqlite. This analysis looks at precipitation and temperature data over the coarse of the year 2016. The Flask Python module was used to display the results in a url (code is found in app.py). 

In another script, SurfsUp_Challenge.ipynb, temeratrue data for the months of June and December are also looked at.  

## Results

![ScreenShot_juneTemps.png](https://github.com/charliuden/Surfs-Up/blob/main/Resources/ScreenShot_juneTemps.png)

![ScreenShot_decemberTemps.png](https://github.com/charliuden/Surfs-Up/blob/main/Resources/ScreenShot_decemberTemps.png)

* The mean temperature in December is just four degrees cooler than in June.
* The maximum temperatrue in December (83°F) is also not much cooler than June's maximum temperature (85°F) - just two degrees cooler. 
* However, December in Oahu can see chilly days -much chillier than in June. The coolest day in December was 56°F, while June's coolest day is 64°F. 

## Summary: 

Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.

* While average temberatures during an Oauhu December do not differ too much from June temperatures, some days can drop to temperatures below 60°F. Is this something that I shuold be worried about - how often do temperatures drop during December? The standard deviation indicates that most of the data is within 3.4°F, so it is likely that these colder December days are infrequent. However, to answer get a clearer anser to this question, I would write a quary to find the total number of december days that drop below 60°F: 

session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date) == 12).filter(Measurement.tobs =< 60).all()

* 
