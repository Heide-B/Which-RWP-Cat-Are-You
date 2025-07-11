import streamlit as st
from utils.util import form_callback

st.header("What Sparks Joy in Your Life")

youth_pick = st.selectbox(
    "7. Pick the thing that excites you the most:",
    [
        "New plushies or fun stickers",
        "A big milestone or achievement",
        "Trying a new outdoor activity",
        "A deep conversation or book discussion"
    ],
    width='stretch'
)

st.container(height=250, border=False)
c1, c2 =  st.columns([0.8, 0.2], vertical_alignment="center")

with c2:
    if st.button(":material/arrow_back: Back", use_container_width=True):
        st.switch_page("pages/q6.py")

with c1:
    if st.button(":material/arrow_forward: Next", use_container_width=True, type="primary", on_click=form_callback, args=(youth_pick,'question7')):
        st.switch_page("pages/q8.py")