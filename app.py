import streamlit as st
import pandas as pd

# setup
teamups = pd.read_csv("teamups.csv")

st.title("Marvel Rivals Team-Up Tracker")

tab_main, tab_data = st.tabs(["Main", "Data"])

with tab_main:
  st.write("Main tab - watch this space")

with tab_data:
  st.dataframe(teamups)
