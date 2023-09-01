import streamlit as st

st.title("Tripadvisor Search")


st.text("This application uses the following to create a restaurant search app:")
st.text("""
>Streamlit 
>Python
>Pandas
>TripAdvisor API """)

st.header("Here are the different pages of the application:")

st.subheader('Base Info')

st.markdown('Queries to pull up general information about a location.')

st.subheader("Restaurant Details")
st.markdown("Returns more specific details about a restaurant by the given query.")

st.subheader("Reviews Search")
st.markdown("Returns number of reviews and average rating for a specific location.")

st.subheader("Summary")
st.markdown("Summary page explaining the intended functionality of the application and the process in which I retrieved the data to be queried.")
