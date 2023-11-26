import streamlit as st
import pandas as pd
import plotly.express as px
import data

st.set_page_config(page_title='Year Wise Analysis')

st.title('Year Wise Analysis')

df = data.load_data()
df.dropna(inplace=True)

fig = px.histogram(df, y="release_year", color="release_year")

fig.show()

st.plotly_chart(fig, use_container_width=True)
