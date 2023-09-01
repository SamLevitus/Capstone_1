import streamlit as st
import requests
 
url = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchLocation"
    
user_input = st.text_input('Enter a restaurant name:', value='Mumbai')

querystring = {"query":{user_input}}

headers = {
    "X-RapidAPI-Key": "5a53242ad0msh2c919b5c9b0e056p1f90b7jsn41087085a5ba",
    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
}

response1 = requests.get(url, headers=headers, params=querystring)
rest_id = response1.json()['data'][0]['locationId']
st.text_input('Please use below ID on the "Details" page:', value=rest_id)
response1.json()

querystring2 = {"query": {rest_id}}

response2 = requests.get(url, headers=headers, params=querystring2)
response2.json()
    
data = response1.json()
data2 = response2.json()

st.title("General Restaurant Information:")
st.write(data)   
                    