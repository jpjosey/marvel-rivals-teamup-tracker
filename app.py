import streamlit as st
import pandas as pd

# setup
heroes = pd.read_csv("heroes.csv")
teamups = pd.read_csv("teamups.csv")

st.title("Marvel Rivals Team-Up Tracker")

tab_main, tab_data = st.tabs(["Main", "Data"])

with tab_main:
  col_settings, col_vanguard, col_duelist, col_strategist = st.columns(4)

  with col_settings:
      st.subheader("Options")
      short_names = st.toggle("Use short hero names", value=True)

  names = "Short_Name" if short_names else "Hero"

  with col_vanguard:
      st.subheader("Vanguard")
      min_vanguard = st.number_input("Min", min_value=0, max_value=6, value=1, key="min_vanguard")
      max_vanguard = st.number_input("Max", min_value=0, max_value=6, value=3, key="max_vanguard")
      vanguard_options = heros.loc[heroes["Role"] == "Vanguard", names].tolist()
      selected_vanguards = st.multiselect("Allowed", options=vanguard_options, default=vanguard_options)
  
  with col_duelist:
      st.subheader("Duelist")
      min_duelist = st.number_input("Min", min_value=0, max_value=6, value=1, key="min_duelist")
      max_duelist = st.number_input("Max", min_value=0, max_value=6, value=3, key="max_duelist")
  
  with col_strategist:
      st.subheader("Strategist")
      min_strategist = st.number_input("Min", min_value=0, max_value=6, value=2, key="min_strategist")
      max_strategist = st.number_input("Max", min_value=0, max_value=6, value=3, key="max_strategist")



with tab_data:
  st.dataframe(teamups)
  st.dataframe(heroes)
