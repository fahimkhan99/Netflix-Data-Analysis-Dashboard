import streamlit as st
import pandas as pd

df = pd.read_csv("netflix_titles.csv")

st.title("Netflix Content Analysis Dashboard")

st.subheader("Movies vs TV Shows")
st.bar_chart(df['type'].value_counts())

st.subheader("Top Countries")
st.bar_chart(df['country'].value_counts().head(10))

st.subheader("Content Growth Over Years")
st.line_chart(df['release_year'].value_counts().sort_index())