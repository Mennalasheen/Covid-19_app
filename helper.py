import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache
def load_data():
    df=pd.read_csv("C:\\Users\\PC\\Downloads\\WHO-COVID-19-global-data.csv")
    df['Date_reported'] = pd.to_datetime(df['Date_reported'])
    return df

df=load_data()

def regionSelected(regions):
    if regions == 'Select Region':
        temp_df = df[(df['WHO_region'].isin(regions))]
    else:
        temp_df = df
    return temp_df

def regionscases(regions,startdate,enddate):

    fig=px.histogram(regionSelected(regions),x='Date_reported',y='New_cases',title="Total cases",range_x=[startdate,enddate],nbins=60)

    return fig

def regiondeaths(regions,startdate,enddate):

  fig=px.histogram(regionSelected(regions),x='Date_reported',y="New_deaths",title='Total deaths',range_x=[startdate,enddate],nbins=60)
  return fig


def countrySelected(countries):
    if countries == 'Select Country':
        temp_df = df[(df['Country'].isin(countries))]
    else:
        temp_df = df
    return temp_df

def countrycases(countries,startdate,enddate):

    fig=px.histogram(countrySelected(countries),x='Date_reported',y='New_cases',title="Total cases",range_x=[startdate,enddate],nbins=60)

    return fig

def countrydeaths(countries,startdate,enddate):

  fig=px.histogram(countrySelected(countries),x='Date_reported',y="New_deaths",title='Total deaths',range_x=[startdate,enddate],nbins=60)
  return fig