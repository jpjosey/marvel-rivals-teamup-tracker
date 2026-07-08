import streamlit as st
import pandas as pd

# setup
heroes = pd.read_csv("heroes.csv")
teamups = pd.read_csv("teamups.csv")

st.title("Marvel Rivals Team-Up Tracker")

tab_main, tab_data = st.tabs(["Main", "Data"])

with tab_main:
  col_vanguard, col_duelist, col_strategist, col_misc = st.columns(3)

  with col_vanguard:
      st.subheader("Vanguard")
      min_vanguard = st.number_input("Min", min_value=0, max_value=6, value=1, key="min_vanguard")
      max_vanguard = st.number_input("Max", min_value=0, max_value=6, value=3, key="max_vanguard")
  
  with col_duelist:
      st.subheader("Duelist")
      min_duelist = st.number_input("Min", min_value=0, max_value=6, value=1, key="min_duelist")
      max_duelist = st.number_input("Max", min_value=0, max_value=6, value=3, key="max_duelist")
  
  with col_strategist:
      st.subheader("Strategist")
      min_strategist = st.number_input("Min", min_value=0, max_value=6, value=2, key="min_strategist")
      max_strategist = st.number_input("Max", min_value=0, max_value=6, value=3, key="max_strategist")

  with col_misc:
      st.subheader("Misc.")
      short_names = st.toggle("Use short hero names", value=True)

with tab_data:
  st.dataframe(teamups)
  st.dataframe(heroes)
