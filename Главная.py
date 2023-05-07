import time
import streamlit as st
import pandas as pd
import numpy as np
import random
import openpyxl

from streamlit import session_state as state

st.set_page_config(page_title='Калькулятор ХВЗК', layout='wide')

st.header("Диагностический калькулятор для оценки формы и стадии воспалительных заболеваний кишечника")
st.subheader("Введите необходимые показатели")
if 'FIO' in state:
    state['FIO']

tab1, tab2, tab3 = st.tabs(["Основные показатели", "Кислоты 1",
                                  "Кислоты 2"])

for key in state.keys():
    if key != 'uploaded':
        state[key] = state[key]
state.update()

with tab1:
    tab1_col1, tab1_col2 = st.columns(2)
    group1 = st.container()
    with group1:
        with tab1_col1:
            st.number_input("Гемоглобин",0.0, 200.0, key = "гемоглобин")
            st.number_input("MCHC", 0.0, 1000.0, key = "mchc")
            st.number_input("Лейкоциты", 0.0, 100.0, key = "лейкоциты")
            st.number_input("Гематокрит", 0.0, 100.0, key = "гематокрит")
            st.number_input("СОЭ", 0.0, 100.0, key = "соэ")
            st.number_input("Кальпротектин", 0.0, 1000.0, key = "кальпротектин")
        with tab1_col2:
            st.number_input("MCV", 0.0, 100.0, key = "mcv")
            st.number_input("СРБ", 0.0, 100.0, key = "срб")
            st.number_input("Фибриноген", 0.0, 100.0, key = "фибриноген")
            st.number_input("MCH", 0.0, 100.0, key = "mch")
            st.number_input("Ферритин", 0.0, 100.0, key = "ферритин")

with tab2:
    tab2_col1, tab2_col2 = st.columns(2)
    group2 = st.container()
    with group2:
        with tab2_col1:
            st.number_input("e c-цис (c-c18:1)", 0.0, 100.0, key="e c-цис (c-c18:1)")
            st.number_input("e 7,10,13,16-c22:4", 0.0, 100.0, key="e 7,10,13,16-c22:4")
            st.number_input("e 11,14-c20:2", 0.0, 100.0, key="e 11,14-c20:2")
            st.number_input("e 5,8,11,14-c20:4", 0.0, 100.0, key="e 5,8,11,14-c20:4")
        with tab2_col2:
            st.number_input("e t-транс (t-c18:1)", 0.0, 100.0, key="e t-транс (t-c18:1)")
            st.number_input("e полиненасыщ", 0.0, 100.0, key = "e полиненасыщ")
            st.number_input("e c12:0", 0.0, 100.0, key = "e c12:0")

with tab3:
    tab3_col1, tab3_col2 = st.columns(2)
    group4 = st.container()
    with group4:
        with tab3_col1:
            st.number_input("s 7,10,13,16-c22:4", 0.0, 10.0, key="s 7,10,13,16-c22:4")
            st.number_input("s 5,8,11,14,17-c20:5", 0.0, 100.0, key="s 5,8,11,14,17-c20:5")
            st.number_input("s 5,8,11,14-c20:4", 0.0, 100.0, key="s 5,8,11,14-c20:4")
            st.number_input("s c12:0", 0.0, 100.0, key="s c12:0")
        with tab3_col2:
            st.number_input("s омега-3", 0.0, 100.0, key="s омега-3")
            st.number_input("s омега-3/омега-6", 0.0, 100.0, key="s омега-6/омега-3")
            st.number_input("s полиненасыщ", 0.0, 100.0, key = "s полиненасыщ")

#df_model1 = pd.DataFrame([[state.hemoglobin_state, state.mcv_state, state.e_cis_18_1_state]],
#                        columns=['Гемоглобин', 'MCV', 'e c-цис (c-c18:1)'])
#df_model2 = pd.DataFrame([[state.hematokrit_state, state.discocyte_state, state.s_t_18_1_state]],
#                        columns=['Гематокрит', 'Доля дискоцитов', 's t-c18:1'])
#df_model3 = pd.DataFrame([[state.ampl_def_state, state.soe_state, state.eritr_speed_state]],
#                        columns=['Ампл деф на 1мгц', 'СОЭ', 'Скорость движения эритроцитов'])
#df_model4 = pd.DataFrame([[state.s_20_5_state, state.s_omega_3_6_state, state.s_poly_state]],
#                        columns=['s 5,8,11,14,17-c20:5', 's омега-3/омега-6', 's полиненасыщ'])
#
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

#def calc(model):
#    res = 0
#    for col in model.keys():
#        res += model.get(col)
#    return healthy(res[0])
#
#diagnose1 = calc(df_model1)
#diagnose2 = calc(df_model2)
#diagnose3 = calc(df_model3)
#diagnose4 = calc(df_model4)

st.subheader("Полученные результаты")
results = st.container()

#with results:
#    c1,c2,c3,c4,c5,c6,c7,c8 = st.columns([3,3,3,3,3,3,3,3])
#    with c1:
#        "**Модель 1:**"
#    with c2:
#        #st.write(diagnose1)
#    with c3:
#        "**Модель 2:**"
#    with c4:
#        #st.write(diagnose2)
#    with c5:
#        "**Модель 3:**"
#    with c6:
#        #st.write(diagnose3)
#    with c7:
#        "**Модель 4:**"
#    with c8:
#        #st.write(diagnose4)

state.update()


