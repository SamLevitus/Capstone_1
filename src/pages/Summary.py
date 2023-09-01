import streamlit as st

st.title('Summary for Restaurant Information Application')

st.text('''
        This multi-page application was designed to allow users to input the name of a specific restaurant and return
        comprehensive information such as the address, ratings and reviews, URLs for the listings, and photos 
        of the location. Also, the visualizations page is intended to be able to filter by food type, average/number of reviews,
        city, and country. Rather than using a database to query, the design of the API is such that I was able to 
        ping it directly to retrieve the desired information. This came with some challenges as most of my experience
        has been working with file paths when building apps. With more time I believe I can make the application much more
        efficient and user-friendly, along with including all of the features I intended.
        '''
        )

st.write('Technologies Used: streamlit, python, pandas')