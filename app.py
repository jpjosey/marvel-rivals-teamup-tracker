import streamlit as st
import pandas as pd

# setup
heroes = pd.read_csv("heroes.csv")
teamups = pd.read_csv("teamups.csv")

st.title("Marvel Rivals Team-Up Tracker")

tab_main, tab_data = st.tabs(["Main", "Data"])

with tab_main:
  col_vanguard, col_duelist, col_strategist = st.columns(3)

  with col_vanguard:
      st.subheader("Vanguards")
      min_vanguard = st.number_input("Min", min_value=0, max_value=6, value=1)
      max_vanguard = st.number_input("Max", min_value=0, max_value=6, value=3)
  
  with col_duelist:
      st.subheader("Duelists")
      min_duelist = st.number_input("Min", min_value=0, max_value=6, value=1)
      max_duelist = st.number_input("Max", min_value=0, max_value=6, value=3)
  
  with col_strategist:
      st.subheader("Strategists")
      min_strategist = st.number_input("Min", min_value=0, max_value=6, value=2)
      max_strategist = st.number_input("Max", min_value=0, max_value=6, value=3)

with tab_data:
  st.dataframe(teamups)
  st.dataframe(heroes)
