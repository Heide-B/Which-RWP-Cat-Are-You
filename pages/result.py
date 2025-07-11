import streamlit as st
import yaml


CFG = yaml.load(open("config/cfg.yml", "r"), Loader=yaml.FullLoader)
try:
    catscores = CFG['cat_scores']
    cat = list(catscores.keys())[list(catscores.values()).index(st.session_state.SCORE)]
except:
    if st.session_state.SOCIAL > 0:
        cat = CFG['social_cats'][st.session_state.RAW_SCORE]
    else:
        cat = CFG['nonsocial_cats'][st.session_state.RAW_SCORE]

st.header("Your RWP cat is:", width="content")
st.title(cat.upper(), width="content")

color = st.image(f"cats/{cat}.jpg", caption="Meow meow")
st.write(f"{CFG['description'][cat]}")
c1, c2 =  st.columns([0.8, 0.2], vertical_alignment="center")

with c2:
    if st.button(":material/replay: Retry the quiz", use_container_width=True):
        st.switch_page("./streamlit_run.py")

with c1:
    if st.button(":material/art_track: See all the RWP Cats", use_container_width=True, type="primary"):
        st.switch_page("pages/inventory.py")