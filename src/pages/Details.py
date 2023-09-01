import streamlit as st
import requests
 
url = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchRestaurants"
    
user_input = st.text_input('Enter restaurant location ID:', value='1806141')

querystring = {"locationId":{user_input}}

headers = {
    "X-RapidAPI-Key": "5a53242ad0msh2c919b5c9b0e056p1f90b7jsn41087085a5ba",
    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

st.title("More Comprehensive Restaurant Information:")
st.write(response.json())   

