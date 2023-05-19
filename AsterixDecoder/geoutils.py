import json
import datetime

def generateGeoJSON(planes):
    
    features = []

    for plane_data in planes:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [plane_data["lon"], plane_data["lat"]]
            },
            "properties": {
                "time": convert_time(plane_data["time"]),
                "plane_id": plane_data["plane_id"],
                "traffic_type": plane_data["traffic_type"],
                "FL": plane_data["FL"]
            }
        }
    features.append(feature)
    
    geojson_data = {
    "type": "FeatureCollection",
    "features": features
}

    with open("data.geojson", "w") as f:
        json.dump(geojson_data, f)
        
def convert_time(seconds):
    current_datetime = datetime.datetime.now()

    current_date = current_datetime.date()
    current_time = current_datetime.time()

    provided_seconds = seconds  # Replace with your provided time in seconds

    new_datetime = datetime.datetime.combine(current_date, datetime.time()) + datetime.timedelta(seconds=provided_seconds)

    # Format the datetime object as an ISO 8601 timestamp
    time_iso8601 = new_datetime.isoformat()

    return(time_iso8601[:19])

