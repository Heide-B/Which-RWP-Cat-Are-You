import streamlit as st
from utils.util import form_callback

st.header("Chill or Action")

chill_response = st.radio(
    "6. How do you usually respond when things don't go as planned?",
    [
        "I stay calm and go with the flow",
        "I try to fix it quickly or find a new plan",
        "I stress out but push through",
        "I need time alone to reset"
    ],
    width="stretch"
)

st.container(height=250, border=False)
c1, c2 =  st.columns([0.8, 0.2], vertical_alignment="center")

with c2:
    if st.button(":material/arrow_back: Back", use_container_width=True):
        st.switch_page("pages/q5.py")

with c1:
    if st.button(":material/arrow_forward: Next", use_container_width=True, type="primary", on_click=form_callback, args=(chill_response,'question6')):
        st.switch_page("pages/q7.py")