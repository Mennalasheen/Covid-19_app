import streamlit as st

import helper
from helper import *
st.title("Covid-19 Data Analysis")
# Corrected image URL
image_url = 'https://logos-world.net/wp-content/uploads/2021/03/World-Health-Organization-WHO-Symbol.png'

st.image(image_url, caption='COVID-19 Image', width=200)
st.header('Description')
st.markdown(''' This app is designed to analyze covid-19 data''')

st.header('Data')
if st.checkbox('Show Data'):
    st.write(helper.df)