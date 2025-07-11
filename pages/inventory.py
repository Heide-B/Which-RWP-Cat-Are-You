import streamlit as st
from glob import glob
import yaml

css = """
.st-container{
    background: rgba(100, 100, 200, 0.3);
}
"""
st.html(f"<style>{css}</style>")

st.title("Meet our RWP Cats", width="content")
CFG = yaml.load(open("config/cfg.yml", "r"), Loader=yaml.FullLoader)

res = glob("cats/*")
row = len(res) % 4
grid = st.columns(row)
col = 0

for cats in res:
    with grid[col]:
        container = grid[col].container(border=True)
        name = cats.split("\\")[-1].split('/')[-1].replace(".jpg","")
        container.image(cats)
        container.write(f"Name: {name}, Meet them at: {CFG['cat_location'][name]}")
    col = (col + 1) % row

if st.button(":material/replay: Retry the quiz", use_container_width=True):
    st.switch_page("./streamlit_run.py")

