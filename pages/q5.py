import streamlit as st
from utils.util import form_callback

st.header("Whats the vibe")

energy = st.radio(
    "5. How do people describe your energy?",
    ["High-energy and always moving",
     "Relaxed and easy-going",
     "Quiet but thoughtful",
     "Playful and bubbly"],
    width='stretch'
)

st.container(height=250, border=False)
c1, c2 =  st.columns([0.8, 0.2], vertical_alignment="center")

with c2:
    if st.button(":material/arrow_back: Back", use_container_width=True):
        st.switch_page("pages/q4.py")

with c1:
    if st.button(":material/arrow_forward: Next", use_container_width=True, type="primary", on_click=form_callback, args=(energy,'question5')):
        st.switch_page("pages/q6.py")