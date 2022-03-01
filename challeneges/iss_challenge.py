#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import time
import urllib.request


URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    result= resp['timestamp']

    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    print('Latitude: ' + str(lat))
    print('Longitude: ' + str(lon))

if __name__ == "__main__":
    main()



    ### Work on Solution###
