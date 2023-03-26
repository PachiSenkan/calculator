import time

import streamlit as st
import pandas as pd
import numpy as np
import random
import openpyxl

st.set_page_config(
  page_title="Калькулятор ХВЗК",
  page_icon="chart_with_upwards_trend",
  initial_sidebar_state="expanded"
)

st.header("Диагностический калькулятор для оценки формы и стадии воспалительных заболеваний кишечника")
st.sidebar.header("Введите необходимые показатели")

tab1, tab2, tab3, tab4 = st.sidebar.tabs(["1 группа", "2 группа", "3 группа", "4 группа"])

sidebar = st.sidebar
with sidebar:
    st.header("Или выберите файл для загрузки")
    uploaded_file = st.file_uploader("Загрузка файла", label_visibility="hidden")
    if uploaded_file is not None:
        df1 = pd.read_excel(uploaded_file)
        statet = st.session_state
        statet.g11 = df1.iloc[0, 0]
        statet.g12 = df1.iloc[0, 1]
        statet.g13 = df1.iloc[0, 2]
        statet.g14 = df1.iloc[0, 3]
        statet.g15 = df1.iloc[0, 4]
        statet.g16 = df1.iloc[0, 5]
        statet.g21 = df1.iloc[0, 6]

    with tab1:
        col11, col21, col31, col41 = st.columns(4)
        group1 = st.container()
        with group1:
            with col11:
                st.number_input("Гемоглобин",0.0, 100.0, key = "g11")
                st.number_input("mchc", 0.0, 100.0, key = "g15")
                st.number_input("лейкоциты", 0.0, 100.0, key = "g19")
                st.number_input("гист акт", 0.0, 100.0, key = "g113")
            with col21:
                st.number_input("гематокрит", 0.0, 100.0, key = "g12")
                st.number_input("соэ", 0.0, 100.0, key = "g16")
                st.number_input("кальпротектин", 0.0, 100.0, key = "g110")
            with col31:
                st.number_input("mcv", 0.0, 100.0, key = "g13")
                st.number_input("срб", 0.0, 100.0, key = "g17")
                st.number_input("фибриноген", 0.0, 100.0, key = "g111")
            with col41:
                st.number_input("mch", 0.0, 100.0, key = "g14")
                st.number_input("ферритин", 0.0, 100.0, key = "g18")
                st.number_input("энд инд акт няк, нкк, бк", 0.0, 100.0, key = "g112")

    with tab2:
        col12, col22, col32, col42 = st.columns(4)
        group2 = st.container()
        with group2:
            with col12:
                st.number_input("ампл деф на 1мгц",0.0, 100.0, key = "g21")
                st.number_input("доля дискоцитов", 0.0, 100.0, key = "g25")
                st.number_input("поляр на 0.05мгц", 0.0, 100.0, key = "g29")
                st.number_input("доля сфероцитов", 0.0, 100.0, key = "g213")
            with col22:
                st.number_input("емкость мембран", 0.0, 100.0, key = "g22")
                st.number_input("поляр на 1мгц", 0.0, 100.0, key = "g26")
                st.number_input("обобщенная жесткость", 0.0, 100.0, key = "g210")
                st.number_input("доля деформир.клеток", 0.0, 100.0, key = "g214")
            with col32:
                st.number_input("дипольный момент", 0.0, 100.0, key = "g23")
                st.number_input("поляр на 0.5мгц", 0.0, 100.0, key = "g27")
                st.number_input("обобщ вязкость", 0.0, 100.0, key = "g211")
                st.number_input("равня частота", 0.0, 100.0, key = "g215")
            with col42:
                st.number_input("ск. движ эр", 0.0, 100.0, key = "g24")
                st.number_input("поляр на 0.1мгц", 0.0, 100.0, key = "g28")
                st.number_input("электропр", 0.0, 100.0, key = "g212")

    with tab3:
        '3'

    with tab4:
        '4'

        #st.session_state.g11 = df1[0,1]

container = st.container()

tab1_main, tab2_main, tab3_main, tab4_main = st.tabs(["1 модель", "2 модель", "3 модель", "4 модель"])
state = st.session_state
df_model1 = pd.DataFrame([[state.g11, state.g16, state.g111]],
                        columns=['Гемоглобин', 'СОЭ', 'Фибриноген'])
df_model2 = pd.DataFrame([[state.g12, state.g25, state.g112]],
                        columns=['гематокрит', 'доля дискоцитов', 'энд инд акт няк, нкк, бк'])
df_model3 = pd.DataFrame([[state.g21, state.g16, state.g24]],
                        columns=['ампл деф на 1мгц', 'СОЭ', 'ск. движ эр'])
df_model4 = pd.DataFrame([[state.g21, state.g26, state.g211]],
                        columns=['ампл деф на 1мгц', 'поляр на 1мгц', 'обобщ вязкость'])

def healthy(res):
    if res == 0:
        return "Здоров:full_moon_with_face:"
    if res > 0 and res < 1:
        return "НЯК ремиссия:ok_hand:"
    if res >= 1 and res < 2:
        return "БК ремиссия:ok_hand:"
    if res >= 2 and res < 3:
        return "НКК ремиссия:ok_hand:"
    if res >= 3 and res < 4:
        return "НЯК обострение:broken_heart:"
    if res >= 4 and res < 5:
        return "БК обострение:broken_heart:"
    if res >= 5:
        return "НКК обострение:broken_heart:"



with tab1_main:
        st.header("Модель 1")
        st.subheader("Введенные показатели")
        df_model1
        st.subheader("Полученное значение")
        res1 = 0
        for col in df_model1.keys():
            res1 += df_model1.get(col)
        diagnose1 = healthy(res1[0])
        st.write(res1)
        st.subheader(diagnose1)

with tab2_main:
        st.header("Модель 2")
        st.subheader("Введенные показатели")
        df_model2
        st.subheader("Полученное значение")
        res2 = 0
        for col in df_model2.keys():
            res2 += df_model2.get(col)
        diagnose2 = healthy(res2[0])
        st.write(res2)
        st.subheader(diagnose2)

with tab3_main:
        st.header("Модель 3")
        st.subheader("Введенные показатели")
        df_model3
        st.subheader("Полученное значение")
        res3 = 0
        for col in df_model3.keys():
            res3 += df_model3.get(col)
        diagnose3 = healthy(res3[0])
        st.write(res3)
        st.subheader(diagnose3)

with tab4_main:
        st.header("Модель 4")
        st.subheader("Введенные показатели")
        df_model4
        st.subheader("Полученное значение")
        res4 = 0
        for col in df_model4.keys():
            res4 += df_model4.get(col)
        diagnose4 = healthy(res4[0])
        st.write(res4)
        st.subheader(diagnose4)

with container:
    all = pd.DataFrame([[diagnose1, diagnose2, diagnose3, diagnose4]],
                       columns=["Модель 1","Модель 2", "Модель 3", "Модель 4"])
    st.table(all)
    st.write("Модель 1:", diagnose1)
    st.write("Модель 2:", diagnose2)
    st.write("Модель 3:", diagnose3)
    st.write("Модель 4:", diagnose4)


session = st.button("Показать")
session_no = st.button("Убрать")
if session:
    st.write(st.session_state)
if session_no:
    session = False



