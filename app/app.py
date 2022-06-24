import streamlit as st
import pandas as pd
import numpy as np

with open("style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("😁 Teeth checking tool")
st.subheader("Искусственный интеллект для анализа состояния зубов по фотографии")

uploaded_file = st.file_uploader("Выберите изображение...", accept_multiple_files=True)

st.button("Проверить!")
