import streamlit as st
from utils.util import form_callback

st.header("Yapper or Listener?")
group_setting = st.selectbox(
    "2. In a group, you usually:",
    ["Lead the conversation and keep things lively",
     "Listen more and observe",
     "Discuss with a few people",
     "Wander off to explore"], width='stretch'
)

st.container(height=200, border=False)
c1, c2 =  st.columns([0.8, 0.2], vertical_alignment="center")
with c2:
    if st.button(":material/arrow_back: Back", use_container_width=True):
        st.switch_page("pages/q1.py")

with c1:
    if st.button(":material/arrow_forward: Next", use_container_width=True, type="primary", on_click=form_callback, args=(group_setting,'question2')):
        st.switch_page("pages/q3.py")