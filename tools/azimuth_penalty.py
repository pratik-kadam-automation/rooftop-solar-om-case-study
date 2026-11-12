"""Rough size of the loss from panel azimuth and tilt.

Uses pvlib clear-sky irradiance and an isotropic sky model to compare a panel facing
the given azimuth against the same tilt facing due south (northern hemisphere).
This is a clear-sky, relative estimate for checking a suspicion. It is not a yield
simulation. For a real figure use measured POA data or a proper design tool.

Azimuth is in degrees from north: 90 east, 180 south, 270 west.
"""
import argparse


def annual_poa_kwh_m2(lat, lon, tilt, azimuth, tz="Asia/Kolkata", year=2021):
    import pandas as pd
    from pvlib import irradiance, location

    loc = location.Location(lat, lon, tz=tz)
    times = pd.date_range(f"{year}-01-01", f"{year}-12-31 23:00", freq="1h", tz=tz)
    cs = loc.get_clearsky(times, model="simplified_solis")
    sp = loc.get_solarposition(times)
    poa = irradiance.get_total_irradiance(
        tilt, azimuth, sp["apparent_zenith"], sp["azimuth"],
        cs["dni"], cs["ghi"], cs["dhi"], model="isotropic")
    return float(poa["poa_global"].fillna(0).sum() / 1000.0)


def relative_to_south(lat, lon, tilt, azimuths, **kw):
    south = annual_poa_kwh_m2(lat, lon, tilt, 180, **kw)
    return [(az, annual_poa_kwh_m2(lat, lon, tilt, az, **kw) / south) for az in azimuths]


def main():
    ap = argparse.ArgumentParser(description="Relative annual POA by azimuth, clear-sky estimate")
    ap.add_argument("--lat", type=float, required=True)
    ap.add_argument("--lon", type=float, required=True)
    ap.add_argument("--tilt", type=float, required=True)
    ap.add_argument("--azimuths", type=float, nargs="+", default=[90, 135, 180, 225, 270])
    ap.add_argument("--tz", default="Asia/Kolkata")
    a = ap.parse_args()
    print(f"latitude {a.lat}, tilt {a.tilt} deg, clear-sky, relative to due south")
    for az, rel in relative_to_south(a.lat, a.lon, a.tilt, a.azimuths, tz=a.tz):
        print(f"azimuth {az:5.0f} deg   {rel * 100:6.1f} %   ({(rel - 1) * 100:+.1f} %)")


if __name__ == "__main__":
    main()
