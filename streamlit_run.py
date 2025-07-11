import streamlit as st

#PAGE CONFIGS
st.set_page_config(page_title="Which RWP Cat Are You", layout="centered")

st.image("rwp_banner.png", use_container_width=True)
st.subheader("Rosewood Pointe is home to several cats. Find out which furbaby speaks to you!")
c1, col, c3 =  st.columns(3)

with col:
    if st.button("Take the Quiz", use_container_width=True, type='primary'):
        st.switch_page("pages/q1.py")

