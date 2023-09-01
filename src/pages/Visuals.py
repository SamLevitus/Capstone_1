import plotly.express as px
from pathlib import Path
import streamlit as st
import pandas as pd
import os

filepath = os.path.join(Path(__file__).parents[1], 'tripadvisor_data.csv')
df = pd.read_csv(filepath, low_memory=False)

vis_to_use = ['scatterplot', 'histogram', 'bar chart']
type_vis = st.selectbox('Select the type of Visualization you would like to see:', options=vis_to_use)

answer = st.selectbox('Select a Column to Visualize on the X-axis:', options=sorted(list(df.columns)))
answer2 = st.selectbox('Select a column to visualize on the Y-axis:', options = sorted(list(df.columns)))
      
st.plotly_chart(px.scatter(df, x=answer, y=answer2, hover_data=['data']), use_container_width=True)
      