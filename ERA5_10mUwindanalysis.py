#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "ea",
    "dataset": "era5",
    "date": "2008-01-01/to/2008-01-31",
    "expver": "1",
    "levtype": "sfc",
    "param": "165.128",
    "grid": "0.25/0.25",
    "area": "72.5/-22/26.5/45.5", 
    "stream": "oper",
    "time": "00:00:00/01:00:00/02:00:00/03:00:00/04:00:00/05:00:00/06:00:00/07:00:00/08:00:00/09:00:00/10:00:00/11:00:00/12:00:00/13:00:00/14:00:00/15:00:00/16:00:00/17:00:00/18:00:00/19:00:00/20:00:00/21:00:00/22:00:00/23:00:00",
    "type": "an",
    "format": "netcdf",
    "target": "ERA5_10mUwindanalysis_2008.nc",
})