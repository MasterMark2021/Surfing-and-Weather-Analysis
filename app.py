#import dependencies
import datetime as dt
import numpy as np
import pandas as pd

#dependencies we need for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#import Flask dependencies 
from flask import Flask, jsonify

#Access to SQLite Database
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect the database into our classes
Base = automap_base()

#Add the following code to reflect the database
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
#session link from Python to our database
session = Session(engine)

#Define the Flask Application
app = Flask(__name__)

#Creating a Flask Route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    n/api/v1.0/precipitation
    n/api/v1.0/stations
    n/api/v1.0/tobs
    n/api/v1.0/temp/start/end
    ''')