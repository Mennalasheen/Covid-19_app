import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

from datetime import datetime
import helper

# Load Data
df = helper.load_data()

# Intro
st.title('Covid-19 Data Analysis')
st.markdown('''
This app is created to analyze the Covid-19 data.
''')

regions_options= st.selectbox('Select Country',['All Countries','Select Country'])
if regions_options=='All Countries':
    countries='All Countries'
else:
    countries=st.multiselect('Select',df['Country'].unique())


startdate=st.date_input('Start date',datetime(2020,1,1))
startdate=pd.to_datetime(startdate)
enddate=st.date_input('End date',datetime(2023,1,1))
enddate=pd.to_datetime(enddate)

st.header('Total Countries cases')
figure=helper.countrycases(countries,startdate,enddate)
st.plotly_chart(figure)

st.header('Total Countries deaths')
figure2=helper.countrydeaths(countries,startdate,enddate)
st.plotly_chart(figure2)