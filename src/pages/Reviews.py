import streamlit as st
import requests
 
url = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/getRestaurantDetails"
    
user_input = st.text_input('Enter restaurant location ID:', value="Restaurant_Review-g1806141-d23845841-Reviews-El_Cuartel_Restaurant_and_Bar-Tanauan_City_Batangas_Province_Calabarzon_Region_")

querystring = {"restaurantsId":{user_input}}

headers = {
	"X-RapidAPI-Key": "5a53242ad0msh2c919b5c9b0e056p1f90b7jsn41087085a5ba",
	"X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

st.title("Restaurant Reviews Information:")
st.write(response.json())


