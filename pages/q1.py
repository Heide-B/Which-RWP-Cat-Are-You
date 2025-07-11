import streamlit as st
from utils.util import form_callback

st.header("TGIF! What're we doin?")

weekend = st.radio(
    "1. Your ideal weekend plan:",
    ["A big party or group hangout",
     "A cozy day indoors with a book or game",
     "Jogging with friends or my pets",
     "Napping and watching cute animal videos"],
    width="stretch"
)

st.container(height=250, border=False)
c1, c2 =  st.columns([0.8, 0.2], vertical_alignment="center")

with c2:
    if st.button(":material/arrow_back: Back", use_container_width=True):
        st.switch_page("./streamlit_run.py")

with c1:
    if st.button(":material/arrow_forward: Next", use_container_width=True, type="primary", on_click=form_callback, args=(weekend,'question1')):
        st.switch_page("pages/q2.py")