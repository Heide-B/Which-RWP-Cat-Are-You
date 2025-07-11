import streamlit as st
from utils.util import form_callback

st.header("Take some time to recharge")

recharge = st.slider(
    "3. How much do you enjoy being alone to recharge? (0 = I hate being alone, 10 = I love being alone)",
    0, 10, 5, help="0 = I hate being alone, 10 = I love being alone",
    width='stretch'
)

st.container(height=250, border=False)
c1, c2 =  st.columns([0.8, 0.2], vertical_alignment="center")

with c2:
    if st.button(":material/arrow_back: Back", use_container_width=True):
        st.switch_page("pages/q2.py")

with c1:
    if st.button(":material/arrow_forward: Next", use_container_width=True, type="primary", on_click=form_callback, args=(recharge,'question3')):
        st.switch_page("pages/q4.py")