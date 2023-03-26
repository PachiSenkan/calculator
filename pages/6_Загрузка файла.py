import time
import streamlit as st
import pandas as pd
import numpy as np
import random
import openpyxl

from streamlit import session_state as state

st.header("Диагностический калькулятор для оценки формы и стадии воспалительных заболеваний кишечника")

st.subheader("Выберите файл для загрузки")

uploaded_file = st.file_uploader("Загрузка файла", label_visibility="hidden")
if uploaded_file is not None:
    sheet = pd.read_excel(uploaded_file)
    sheet.iloc[0]
    sheet.iloc[1]
