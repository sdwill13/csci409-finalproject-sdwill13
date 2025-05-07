from fastapi import FastAPI
"""For the Lines"""
from lines import line_main
"""For the List of Stations"""
from stations_mgt import list_main
"""For Individual Stations"""
from stationinfo import stationinfo_main

app = FastAPI()


app.mount("/json/jLines", line_main.line_app)
app.mount("/json/jStations", list_main.stationlist_app)
app.mount("/json/jStationInfo", stationinfo_main.station_app)
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI Application's Final Project"}
