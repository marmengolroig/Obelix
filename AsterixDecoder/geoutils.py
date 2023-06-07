import json
import datetime

def generateGeoJSON(plane_data):
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [plane_data["lon"], plane_data["lat"]]
        },
        "properties": {
            "time": convert_time(plane_data["time"]),
            "plane_id": plane_data["plane_id"],
            "tooltip": f'{plane_data["traffic_type"]}\n ID: {plane_data["plane_id"]} \n FL: {plane_data["FL"]}',
            "FL": plane_data["FL"]
        }
    }
    return feature
        
def convert_time(seconds):
    current_datetime = datetime.datetime.now()

    current_date = current_datetime.date()
    current_time = current_datetime.time()

    provided_seconds = seconds  # Replace with your provided time in seconds

    new_datetime = datetime.datetime.combine(current_date, datetime.time()) + datetime.timedelta(seconds=provided_seconds)

    # Format the datetime object as an ISO 8601 timestamp
    time_iso8601 = new_datetime.isoformat()

    return(time_iso8601[:19])

