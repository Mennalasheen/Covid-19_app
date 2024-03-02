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

regions_options= st.selectbox('Select Region',['All Regions','Select Region'])
if regions_options=='All Regions':
    regions='All Regions'
else:
    regions=st.multiselect('Select',df['WHO_region'].unique())


startdate=st.date_input('Start date',datetime(2020,1,1))
startdate=pd.to_datetime(startdate)
enddate=st.date_input('End date',datetime(2023,1,1))
enddate=pd.to_datetime(enddate)

st.header('Total Regions cases')
figure=helper.regionscases(regions,startdate,enddate)
st.plotly_chart(figure)

st.header('Total Regions deaths')
figure2=helper.regiondeaths(regions,startdate,enddate)
st.plotly_chart(figure2)