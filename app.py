import streamlit as st
import pandas as pd

# setup
heroes = pd.read_csv("heroes.csv")
teamups = pd.read_csv("teamups.csv")

st.title("Marvel Rivals Team-Up Tracker")

tab_main, tab_data = st.tabs(["Main", "Data"])

with tab_main:
  col_settings, col_vanguard, col_duelist, col_strategist, col_teamups = st.columns(5)

  with col_settings:
      st.subheader("Options")
      short_names = st.toggle("Use short hero names", value=True)

  
  names = "Short_Name" if short_names else "Hero"
  heroes = heroes.sort_values(names)

  name_map = dict(zip(heroes["Hero"], heroes[names]))
  teamup_options = sorted(
    f"{row.Teamup_Name} ({name_map.get(row.Hero_Anchor, row.Hero_anchor)}|{name_map.get(row.Hero_Partner, row.Hero_Partner)}"
    for row in teamups.itertuples()
  )
  

  with col_vanguard:
      st.subheader("Vanguard")
      min_vanguard = st.number_input("Min", min_value=0, max_value=6, value=1, key="min_vanguard")
      max_vanguard = st.number_input("Max", min_value=0, max_value=6, value=3, key="max_vanguard")
      vanguard_options = heroes.loc[heroes["Role"] == "Vanguard", names].tolist()
      selected_vanguards = st.multiselect("Allowed", options=vanguard_options, default=vanguard_options)
  
  with col_duelist:
      st.subheader("Duelist")
      min_duelist = st.number_input("Min", min_value=0, max_value=6, value=1, key="min_duelist")
      max_duelist = st.number_input("Max", min_value=0, max_value=6, value=3, key="max_duelist")
      duelist_options = heroes.loc[heroes["Role"] == "Duelist", names].tolist()
      selected_duelists = st.multiselect("Allowed", options=duelist_options, default=duelist_options)
  
  with col_strategist:
      st.subheader("Strategist")
      min_strategist = st.number_input("Min", min_value=0, max_value=6, value=2, key="min_strategist")
      max_strategist = st.number_input("Max", min_value=0, max_value=6, value=3, key="max_strategist")
      strategist_options = heroes.loc[heroes["Role"] == "Strategist", names].tolist()
      selected_strategist = st.multiselect("Allowed", options=strategist_options, default=strategist_options)

  with col_teamups:
      st.subheader("Team-Ups")
      min_teamups = st.number_input("Min. Enhanced", min_value=0, max_value=6, value=3, key="min_teamups")
      max_teamups = st.number_input("Max. Enhanced", min_value=0, max_value=6, value=6, key="min_teamups")
      selected_teamups = multiselect("Allowed", option=teamup_options, default=teamup_options)



with tab_data:
  st.dataframe(teamups)
  st.dataframe(heroes)
