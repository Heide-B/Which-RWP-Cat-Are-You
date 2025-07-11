import streamlit as st
from utils.util import form_callback

st.header("Where to chill?")

environment = st.selectbox(
    "4. Which of these environments do you enjoy the most?",
    ["A buzzing cafe", "A quiet cabin", "An open beach", "A plush room"],
    width='stretch'
)

st.container(height=250, border=False)
c1, c2 =  st.columns([0.8, 0.2], vertical_alignment="center")

with c2:
    if st.button(":material/arrow_back: Back", use_container_width=True):
        st.switch_page("pages/q3.py")

with c1:
    if st.button(":material/arrow_forward: Next", use_container_width=True, type="primary", on_click=form_callback, args=(environment,'question4')):
        st.switch_page("pages/q5.py")