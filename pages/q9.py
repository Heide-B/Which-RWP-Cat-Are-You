import streamlit as st
import yaml

st.header("Pick your favorite color!")
color = st.color_picker("Pick A Color", "#51C9E0", key='color', width='stretch')

st.container(height=250, border=False)
c1, c2 =  st.columns([0.8, 0.2], vertical_alignment="center")
CFG = yaml.load(open("config/cfg.yml", "r"), Loader=yaml.FullLoader)
st.session_state.SCORE = ""
st.session_state.SOCIAL = 0
st.session_state.RAW_SCORE = 0
for q in CFG['q_answers']:
    answer = st.session_state[q]
    if isinstance(answer, list):
        answer = answer[0]

    if answer in CFG['q_answers'][q]:
        st.session_state.SCORE += "1"
        if q in ['question1','question2','question5','question4']:
            st.session_state.SOCIAL += 1
            st.session_state.RAW_SCORE += 1
    else:
        st.session_state.SCORE += "0"

with c2:
    if st.button(":material/arrow_back: Back", use_container_width=True):
        st.switch_page("pages/part8.py")

with c1:
    if st.button(":material/favorite: See Your Cat!", use_container_width=True, type="primary"):
        st.switch_page("pages/result.py")