import pandas as pd 
import streamlit as st
import plotly.express as px 
# read tips dataframe

data = pd.read_csv('onlinefoods.csv')
# streamlit dataframe
st.dataframe(data)
