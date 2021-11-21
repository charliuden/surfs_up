#-------------------
# Module 9.4: displaying analysis in a url using Flask
# Nov. 20 2021
# Charlotte Uden
#-------------------


import datetime as dt
import numpy as np
import pandas as pd
#import dependancies for accessing sql database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import flask
from flask import Flask, jsonify

#set up our database engine for the Flask application (allows you to access the sql databaase)
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect engine into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link from python to the database
session = Session(engine)

# -- define app for flask --
# create instance (singular version of something)
# dunder - variable name with double underscore: name of current funciton 
# dunder is a magic method. 
# used to determine if your code is being run from the command line or if it has been imported into another piece of code
app = Flask(__name__)

# -- Define Welcome Route --
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# -- Precipirtaion Route  --
        # 1. calculate the date one year ago from the most recent date in the database
        # 2. get the date and precipitation for the previous year.
        # 3. create a dictionary with the date as the key and the precipitation as the value
        # 4. jsonify - make the dictionary into a json file
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# -- Stations Route --
        # 1. get all stations in database
        # 2. use the function np.ravel(), with results as our parameter to unravel results into 1-D array, then use list() to turn array into a list
        # 3. jsonify
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# -- temperature observations ('tobs') --
        # 1. calculate the date one year ago from the last date in the database
        # 2. query the primary station for all the temperature observations from the previous year
        # 3. unravel the results into a one-dimensional array and convert that array into a list
        # 4. jsonify
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# -- minimum, maximum, and average temperatures --
        # 1. add parameters to our stats()function: a start parameter and an end parameter

        # oupput in browser will have null values unless you add a start and end date to url, for example: /api/v1.0/temp/2017-06-01/2017-06-30

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)



# to run this in terminatl and get the app running, enter 'export FLASK_APP=app.py' into the command line
# followed by 'flask run' 
# copy the url into your browser to see the app as a web page. 