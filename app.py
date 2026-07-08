import streamlit as st

st.title("Marvel Rivals Team-Up Tracker")

tab_main, tab_data = st.tabs(["Main", "Data"])

with tab_main:
  st.write("Main tab - watch this space")

with tab_data:
  st.write("Data go here soon")
