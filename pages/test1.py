import time

import streamlit as st
import pandas as pd
import numpy as np
import random

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

button_main = st.button("Рассчитать все")

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
        return "Здоров"
    if res > 0 and res < 1:
        return "НЯК ремиссия"
    if res >= 1 and res < 2:
        return "БК ремиссия"
    if res >= 2 and res < 3:
        return "НКК ремиссия"
    if res >= 3 and res < 4:
        return "НЯК обострение"
    if res >= 4 and res < 5:
        return "БК обострение"
    if res >= 5:
        return "НКК обострение"



with tab1_main:
    model1 = st.form("Модель 1")
    with model1:
        st.header("Модель 1")
        st.subheader("Введенные показатели")
        df_model1
        submit_form1 = st.form_submit_button("Рассчитать")
        if submit_form1 or button_main:
            st.subheader("Полученное значение")
            res1 = 0
            for col in df_model1.keys():
                res1 += df_model1.get(col)
            diagnose1 = res1[0]
            st.write(res1)
            st.write(diagnose1)

with tab2_main:
    model2 = st.form("Модель 2")
    with model2 or button_main:
        st.header("Модель 2")
        st.subheader("Введенные показатели")
        df_model2
        submit_form2 = st.form_submit_button("Рассчитать")
        if submit_form2:
            st.subheader("Полученное значение")
            res2 = 0
            for col in df_model2.keys():
                res2 += df_model2.get(col)
            diagnose2 = res2[0]
            st.write(res2)
            st.write(diagnose2)

with tab3_main:
    model3 = st.form("Модель 3")
    with model3 or button_main:
        st.header("Модель 3")
        st.subheader("Введенные показатели")
        df_model3
        submit_form3 = st.form_submit_button("Рассчитать")
        if submit_form3:
            st.subheader("Полученное значение")
            res3 = 0
            for col in df_model3.keys():
                res3 += df_model3.get(col)
            diagnose3 = res3[0]
            st.write(res3)
            st.write(diagnose3)

with tab4_main:
    model4 = st.form("Модель 4")
    with model4:
        st.header("Модель 4")
        st.subheader("Введенные показатели")
        df_model4
        submit_form4 = st.form_submit_button("Рассчитать")
        if submit_form4 or button_main:
            st.subheader("Полученное значение")
            res4 = 0
            for col in df_model4.keys():
                res4 += df_model4.get(col)
            diagnose4 = res4[0]
            st.write(res4)
            st.write(diagnose4)

with container:
    if submit_form1 or button_main:
        st.write("1 модель:", diagnose1)
    else:
        st.write("1 модель:")
    if submit_form2 or button_main:
        st.write("2 модель:", diagnose2)
    else:
        st.write("2 модель:")
    if submit_form3 or button_main:
        st.write("3 модель:", diagnose3)
    else:
        st.write("3 модель:")
    if submit_form4 or button_main:
        st.write("4 модель:", diagnose4)
    else:
        st.write("4 модель:")

session = st.button("Показать")
session_no = st.button("Убрать")
if session:
    st.write(st.session_state)
if session_no:
    session = False



