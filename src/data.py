import requests
import pandas as pd
import streamlit

url = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchRestaurants"

querystring = {"locationId":"304554"}

headers = {
	"X-RapidAPI-Key": "5a53242ad0msh2c919b5c9b0e056p1f90b7jsn41087085a5ba",
	"X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)



df= pd.DataFrame.from_dict(response.json()['data']['restaurantsId'])

df.to_csv('src/tripadvisor_data.csv',index=False)