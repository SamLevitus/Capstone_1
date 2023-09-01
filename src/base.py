import pandas as pd
import requests
import urllib.request, json
from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth
import numpy as np
from urllib.request import Request, urlopen
from urllib.error import URLError

from tripadvisorapi.api import TripadvisorApi as taa
class Base:
    def __init__(self):
        self.api_url = "https://tripadvisor16.p.rapidapi.com/?api_key=5a53242ad0msh2c919b5c9b0e056p1f90b7jsn41087085a5ba/"
               
    def return_url(self):
        return self.api_url
                        
    def rest_locations(self):
        url = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchLocation"

        loc_input = input('Please enter a location by city:')

        querystring = {"query":"{loc_input}"}
        headers = {
            "X-RapidAPI-Key": "5a53242ad0msh2c919b5c9b0e056p1f90b7jsn41087085a5ba",
            "X-RapidAPI-Host": "https://tripadvisor16.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        print(response.json())
                    
    def rest():
        url = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchRestaurants"

        querystring = {"locationId":"304554"}
        headers = {
            "X-RapidAPI-Key": "5a53242ad0msh2c919b5c9b0e056p1f90b7jsn41087085a5ba",
            "X-RapidAPI-Host": "https://tripadvisor16.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        print(response.json())

    def rest_details():

        url = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/getRestaurantDetails"

        querystring = {"restaurantsId":"Restaurant_Review-g304554-d8010527-Reviews-Saptami-Mumbai_Maharashtra","currencyCode":"USD"}
        headers = {
            "X-RapidAPI-Key": "5a53242ad0msh2c919b5c9b0e056p1f90b7jsn41087085a5ba",
            "X-RapidAPI-Host": "https://tripadvisor16.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        print(response.json())

    def nearby():
        url = "https://api.content.tripadvisor.com/api/v1/location/nearby_search?language=en"

        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        print(response.text)  

    def reviews():
        url = "https://api.content.tripadvisor.com/api/v1/location/locationId/reviews?language=en"

        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        print(response.text)

if __name__ == '__main__':
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchRestaurants"

    querystring = {"locationId":"304554"}
    headers = {
	    "X-RapidAPI-Key": "5a53242ad0msh2c919b5c9b0e056p1f90b7jsn41087085a5ba",
	    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    # t = taa("5a53242ad0msh2c919b5c9b0e056p1f90b7jsn41087085a5ba")
    # r = t.location_search('Los Angeles')
    # print(json.loads(r.text))