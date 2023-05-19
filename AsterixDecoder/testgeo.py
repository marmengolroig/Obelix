import pymap3d as pm

ell = pm.Ellipsoid.from_name('wgs84')

e=285
n=1020
u=0
lat0=41.296944
lon0=2.078333
h0=0

lat, lon, alt = pm.enu2geodetic(e, n, u, lat0, lon0, h0, ell, deg=True)

print(lat,lon,alt)