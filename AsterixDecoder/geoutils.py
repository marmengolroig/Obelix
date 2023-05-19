import math
import pyproj

def localCartesian2ECEF(easting,northing,up,ref_lon,ref_lat,ref_height):
    a = 6378137.0  # Earth's semi-major axis (meters)
    e = 0.0818191908426  # Earth's eccentricity
    ref_lon=ref_lon*math.pi/180
    ref_lat=ref_lat*math.pi/180

    N = a / math.sqrt(1 - (e * math.sin(ref_lat)) ** 2)  # Radius of curvature in the prime vertical

    ref_x_ecef = (N + ref_height) * math.cos(ref_lat) * math.cos(ref_lon)
    ref_y_ecef = (N + ref_height) * math.cos(ref_lat) * math.sin(ref_lon)
    ref_z_ecef = ((1 - e ** 2) * N + ref_height) * math.sin(ref_lat)

    # Convert local ENU coordinates to ECEF
    cos_lon = math.cos(ref_lon)
    sin_lon = math.sin(ref_lon)
    cos_lat = math.cos(ref_lat)
    sin_lat = math.sin(ref_lat)

    x_ecef = ref_x_ecef - sin_lon * easting - cos_lon * sin_lat * northing + cos_lon * cos_lat * up
    y_ecef = ref_y_ecef + cos_lon * easting - sin_lon * sin_lat * northing + cos_lon * sin_lat * up
    z_ecef = ref_z_ecef + cos_lat * northing + sin_lat * up

    return (x_ecef,y_ecef,z_ecef)

def ECEF2geodesic(x_ecef,y_ecef,z_ecef):
    ecef_to_wgs84 = pyproj.Transformer.from_crs('EPSG:4978', 'EPSG:4326', always_xy=True)

    # Convert ECEF coordinates to WGS84 geodesic coordinates
    lon, lat, height = ecef_to_wgs84.transform(x_ecef, y_ecef, z_ecef)

    return (lon,lat,height)

# ecef = localCartesian2ECEF(285,1020,0,41.296944,2.078333,0)
# geodesic = ECEF2geodesic(ecef[0],ecef[1],ecef[2])
# print(geodesic)