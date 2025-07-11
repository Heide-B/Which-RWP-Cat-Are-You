import streamlit as st
from utils.util import form_callback

st.header("CHONK or SLINK")

cute_scale = st.slider(
    "8. How much do you like cute/chubby things? (0 = Not at all, 10 = I live for CHONKY things!)",
    0, 10, 5, help="0 = Not at all, 10 = I live for cute things!",
    width='stretch'
)

st.container(height=250, border=False)
c1, c2 =  st.columns([0.8, 0.2], vertical_alignment="center")

with c2:
    if st.button(":material/arrow_back: Back", use_container_width=True):
        st.switch_page("pages/q7.py")

with c1:
    if st.button(":material/arrow_forward: Next", use_container_width=True, type="primary", on_click=form_callback, args=(cute_scale,'question8')):
        st.switch_page("pages/q9.py")