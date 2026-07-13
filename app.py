import streamlit as st
import pandas as pd
import itertools

# setup
heroes = pd.read_csv("heroes.csv")
teamups = pd.read_csv("teamups.csv")
st.set_page_config(layout="wide")

st.title("Marvel Rivals Team-Up Tracker")

tab_main, tab_data = st.tabs(["Main", "Data"])

with tab_main:
  col_settings, col_vanguard, col_duelist, col_strategist, col_teamups, col_go = st.columns(6)

  with col_settings:
      st.subheader("Options")
      short_names = st.toggle("Use short hero names", value=True)

  
  names = "Short_Name" if short_names else "Hero"
  heroes = heroes.sort_values(names)

  name_map = dict(zip(heroes["Hero"], heroes[names]))
  teamup_options = sorted(
    f"{row.Teamup_Name} ({name_map.get(row.Hero_Anchor, row.Hero_Anchor)}|{name_map.get(row.Hero_Partner, row.Hero_Partner)})"
    for row in teamups.itertuples()
  )
  

 with col_vanguard:
    st.subheader("Vanguard")
    min_vanguard = st.number_input("Min", min_value=0, max_value=6, value=2, key="min_vanguard")
    max_vanguard = st.number_input("Max", min_value=0, max_value=6, value=2, key="max_vanguard")
    vanguard_options = heroes.loc[heroes["Role"] == "Vanguard", names].tolist()
    selected_vanguards = st.multiselect("Allowed", options=vanguard_options, default=vanguard_options)
    must_vanguards = st.multiselect("Must include", options=vanguard_options, key="must_vanguard")

with col_duelist:
    st.subheader("Duelist")
    min_duelist = st.number_input("Min", min_value=0, max_value=6, value=2, key="min_duelist")
    max_duelist = st.number_input("Max", min_value=0, max_value=6, value=2, key="max_duelist")
    duelist_options = heroes.loc[heroes["Role"] == "Duelist", names].tolist()
    selected_duelists = st.multiselect("Allowed", options=duelist_options, default=duelist_options)
    must_duelists = st.multiselect("Must include", options=duelist_options, key="must_duelist")

with col_strategist:
    st.subheader("Strategist")
    min_strategist = st.number_input("Min", min_value=0, max_value=6, value=2, key="min_strategist")
    max_strategist = st.number_input("Max", min_value=0, max_value=6, value=2, key="max_strategist")
    strategist_options = heroes.loc[heroes["Role"] == "Strategist", names].tolist()
    selected_strategist = st.multiselect("Allowed", options=strategist_options, default=strategist_options)
    must_strategists = st.multiselect("Must include", options=strategist_options, key="must_strategist")

  with col_teamups:
      st.subheader("Team-Ups")
      min_teamups = st.number_input("Min. Enhanced", min_value=0, max_value=6, value=6, key="min_teamups")
      #max_teamups = st.number_input("Max. Enhanced", min_value=0, max_value=6, value=6, key="max_teamups")
      #selected_teamups = st.multiselect("Allowed", options=teamup_options, default=teamup_options)

  with col_go:
      st.subheader("GO!")
      st.write("Warning, insufficient constraints may return literally millions of compositions. Do you hate the rainforest bro?")
      go_pressed = st.button("Go")
  
  if go_pressed:
    must_v = set(must_vanguards)
    must_d = set(must_duelists)
    must_s = set(must_strategists)
    deadpools = {name_map.get(h, h) for h in ["Deadpool (Vanguard)", "Deadpool (Duelist)", "Deadpool (Strategist)"]}
    # teamups keyed by anchor display name
    anchor_map = {}
    for row in teamups.itertuples():
        a = name_map.get(row.Hero_Anchor, row.Hero_Anchor)
        p = name_map.get(row.Hero_Partner, row.Hero_Partner)
        anchor_map.setdefault(a, []).append((row.Teamup_Name, p))

    results = []
    for n_v in range(min_vanguard, max_vanguard + 1):
        for n_d in range(min_duelist, max_duelist + 1):
            n_s = 6 - n_v - n_d
            if not (min_strategist <= n_s <= max_strategist):
                continue
            for vs in itertools.combinations(selected_vanguards, n_v):
                if not must_v <= set(vs):
                    continue
                for ds in itertools.combinations(selected_duelists, n_d):
                    if not must_d <= set(ds):
                        continue
                    for ss in itertools.combinations(selected_strategist, n_s):
                        if not must_s <= set(ss):
                            continue
                        comp = vs + ds + ss
                        n_teamups = 0
                        row_out = {"Comp": f"{n_v}-{n_d}-{n_s}"}
                        for i, hero in enumerate(comp, start=1):
                            cell = ""
                            for t_name, partner in anchor_map.get(hero, []):
                                if partner in members:
                                    cell = f"{t_name} ({partner})"
                                    n_teamups += 1
                                    break
                            row_out[f"Hero{i}"] = hero
                            row_out[f"H{i} Teamup"] = cell
                        if min_teamups <= n_teamups <= 6:
                            row_out["Num Teamups"] = n_teamups
                            results.append(row_out)

    result_df = pd.DataFrame(results)
    st.write(f"{len(result_df):,} compositions found")
    st.dataframe(result_df)



with tab_data:
  st.dataframe(teamups)
  st.dataframe(heroes)
