from fastapi import FastAPI, Depends
import requests
from fastapi.responses import JSONResponse

from configuration.config import ServerSettings, Message
from security.auth import authenticate

line_app = FastAPI()

def build_server_config():
    return ServerSettings()

@line_app.get("/",
    responses={
        400: {"model": Message},
        403: {"model": Message},
        429: {"model": Message}
    }
)
def get_lines(sconfig: ServerSettings = Depends(build_server_config), user: dict = Depends(authenticate)):
    url = f"{sconfig.endpoint}/json/jLines?api_key={sconfig.api_key}"
    response = requests.get(url)

    if response.status_code == 400:
        return JSONResponse(status_code=400, content={"message": "Bad Request"})
    elif response.status_code == 403:
        return JSONResponse(status_code=403, content={"message": "API Request Forbidden"})
    elif response.status_code == 429:
        return JSONResponse(status_code=429, content={"message": "Too Many Requests"})

    try:
        lines = response.json()["Lines"]
    except KeyError:
        return JSONResponse(status_code=500, content={"message": "Unexpected response structure"})

    lines_list = []
    for line in lines:
        lines_list.append({
            "LineCode": line.get("LineCode"),
            "DisplayName": line.get("DisplayName"),
            "StartStationCode": line.get("StartStationCode"),
            "EndStationCode": line.get("EndStationCode"),
            "InternalDestination1": line.get("InternalDestination1"),
            "InternalDestination2": line.get("InternalDestination2"),
        })

    return {"lines": lines_list}
