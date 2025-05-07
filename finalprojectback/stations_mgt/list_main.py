from fastapi import FastAPI, Depends
import requests

from configuration.config import ServerSettings, Message
from security.auth import authenticate
from fastapi.responses import JSONResponse

stationlist_app = FastAPI()

def build_server_config():
    return ServerSettings()

@stationlist_app.get("/{line_code}",
    responses={
        400: {"model": Message},
        403: {"model": Message},
        404: {"model": Message},
        429: {"model": Message}
    }
)
def get_stations_by_line(line_code: str,
                         sconfig: ServerSettings = Depends(build_server_config),
                         user: dict = Depends(authenticate)):
    """Fetches stations for each line : 'BL', 'GR', blah blah blah."""
    url = f"{sconfig.endpoint}/json/jStations?LineCode={line_code}"
    headers = {"api_key": sconfig.api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 400:
        return JSONResponse(status_code=400, content={"message": "Bad Request"})
    elif response.status_code == 403:
        return JSONResponse(status_code=403, content={"message": "API Request Forbidden"})
    elif response.status_code == 404:
        return JSONResponse(status_code=404, content={"message": f"Line {line_code} not found"})
    elif response.status_code == 429:
        return JSONResponse(status_code=429, content={"message": "Too Many Requests"})

    station_data = response.json().get("Stations", [])
    station_list = []

    for station in station_data:
        station_list.append({
            "StationCode": station["Code"],
            "Name": station["Name"],
            "Lat": station["Lat"],
            "Lon": station["Lon"]
        })

    return {"stations": station_list}
