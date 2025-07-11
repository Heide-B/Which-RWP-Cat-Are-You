import streamlit as st


def form_callback(val, question):
    st.session_state[question] = val