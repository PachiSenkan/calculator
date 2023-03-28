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

tab1, tab2, tab3, tab4 = st.tabs(["1 группа показателей", "2 группа показателей",
                                  "3 группа показателей", "4 группа показателей"])

for key in state.keys():
    if key != 'uploaded':
        state[key] = state[key]
state.update()

with tab1:
    tab1_col1, tab1_col2 = st.columns(2)
    group1 = st.container()
    with group1:
        with tab1_col1:
            st.number_input("Гемоглобин",0.0, 100.0, key = "hemoglobin_state")
            st.number_input("MCHC", 0.0, 100.0, key = "mchc_state")
            st.number_input("Лейкоциты", 0.0, 100.0, key = "leukocyte_state")
            st.number_input("Гист акт", 0.0, 100.0, key = "hist_act_state")
            st.number_input("Гематокрит", 0.0, 100.0, key = "hematokrit_state")
            st.number_input("СОЭ", 0.0, 100.0, key = "soe_state")
            st.number_input("Кальпротектин", 0.0, 100.0, key = "calcoprotein_state")
        with tab1_col2:
            st.number_input("MCV", 0.0, 100.0, key = "mcv_state")
            st.number_input("СРБ", 0.0, 100.0, key = "srb_state")
            st.number_input("Фибриноген", 0.0, 100.0, key = "fibrinogen_state")
            st.number_input("MCH", 0.0, 100.0, key = "mch_state")
            st.number_input("Ферритин", 0.0, 100.0, key = "ferritin_state")
            st.number_input("Энд инд акт НЯК, НКК, БК", 0.0, 100.0, key = "end_ind_akt_state")

with tab2:
    tab2_col1, tab2_col2 = st.columns(2)
    group2 = st.container()
    with group2:
        with tab2_col1:
            st.number_input("Ампл деф на 1 МГц",0.0, 100.0, key = "ampl_def_state")
            st.number_input("Доля дискоцитов", 0.0, 100.0, key = "discocyte_state")
            st.number_input("Поляр на 1 МГц", 0.0, 100.0, key="polar_1_state")
            st.number_input("Поляр на 0.5 МГц", 0.0, 100.0, key="polar_05_state")
            st.number_input("Поляр на 0.1 МГц", 0.0, 100.0, key="polar_01_state")
            st.number_input("Поляр на 0.05 МГц", 0.0, 100.0, key="polar_005_state")
            st.number_input("Обобщенная жесткость", 0.0, 100.0, key = "gen_digity_state")
            st.number_input("Доля деформир.клеток", 0.0, 100.0, key = "deformed_part_state")
        with tab2_col2:
            st.number_input("Дипольный момент", 0.0, 100.0, key = "dipole_moment_state")
            st.number_input("Доля сфероцитов", 0.0, 100.0, key="spherocyte_state")
            st.number_input("Обобщенная вязкость", 0.0, 100.0, key = "viscosity_part_state")
            st.number_input("Равня частота", 0.0, 100.0, key = "freq_state")
            st.number_input("Скорость движения эритроцитов", 0.0, 100.0, key = "eritr_speed_state")
            st.number_input("Емкость мембран", 0.0, 100.0, key="membrane_capacity_state")
            st.number_input("Электропроводность", 0.0, 100.0, key = "conductivity_state")

with tab3:
    tab3_col1, tab3_col2 = st.columns(2)
    group3 = st.container()
    with group3:
        with tab3_col1:
            st.number_input("e c-цис (c-c18:1)", 0.0, 100.0, key="e_cis_18_1_state")
            st.number_input("e 7,10,13,16-c22:4", 0.0, 100.0, key="e_22_4_state")
            st.number_input("e 11,14-c20:2", 0.0, 100.0, key="e_20_2_state")
            st.number_input("e 5,8,11,14-c20:4", 0.0, 100.0, key="e_20_4_state")
            st.number_input("e 5,8,11,14,17-c20:5", 0.0, 100.0, key="e_20_5_state")
            st.number_input("e c12:0", 0.0, 100.0, key = "e_12_0_state")
        with tab3_col2:
            st.number_input("e t-транс (t-c18:1)", 0.0, 100.0, key="e_trans_18_1_state")
            st.number_input("e омега-3", 0.0, 100.0, key="e_omega_3_state")
            st.number_input("e омега-3/омега-6", 0.0, 100.0, key="e_omega_3_6_state")
            st.number_input("e омега-3(epa+dha)", 0.0, 100.0, key="e_omega_3_epa_dha_state")
            st.number_input("e полиненасыщ", 0.0, 100.0, key = "e_poly_state")

with tab4:
    tab4_col1, tab4_col2 = st.columns(2)
    group4 = st.container()
    with group4:
        with tab4_col1:
            st.number_input("s c-c18:1", 0.0, 100.0, key="s_c_18_1_state")
            st.number_input("s 7,10,13,16-c22:4", 0.0, 100.0, key="s_22_4_state")
            st.number_input("s 5,8,11,14,17-c20:5", 0.0, 100.0, key="s_20_5_state")
            st.number_input("s 5,8,11,14-c20:4", 0.0, 100.0, key="s_20_4_state")
            st.number_input("s 11,14-c20:2", 0.0, 100.0, key="s_20_2_state")
            st.number_input("s c12:0", 0.0, 100.0, key="s_12_0_state")

        with tab4_col2:
            st.number_input("s t-c18:1", 0.0, 100.0, key="s_t_18_1_state")
            st.number_input("s омега-3", 0.0, 100.0, key="s_omega_3_state")
            st.number_input("s омега-3/омега-6", 0.0, 100.0, key="s_omega_3_6_state")
            st.number_input("s омега-3(epa+dha)", 0.0, 100.0, key="s_omega_3_epa_dha_state")
            st.number_input("s полиненасыщ", 0.0, 100.0, key = "s_poly_state")

df_model1 = pd.DataFrame([[state.hemoglobin_state, state.mcv_state, state.e_cis_18_1_state]],
                        columns=['Гемоглобин', 'MCV', 'e c-цис (c-c18:1)'])
df_model2 = pd.DataFrame([[state.hematokrit_state, state.discocyte_state, state.s_t_18_1_state]],
                        columns=['Гематокрит', 'Доля дискоцитов', 's t-c18:1'])
df_model3 = pd.DataFrame([[state.ampl_def_state, state.soe_state, state.eritr_speed_state]],
                        columns=['Ампл деф на 1мгц', 'СОЭ', 'Скорость движения эритроцитов'])
df_model4 = pd.DataFrame([[state.s_20_5_state, state.s_omega_3_6_state, state.s_poly_state]],
                        columns=['s 5,8,11,14,17-c20:5', 's омега-3/омега-6', 's полиненасыщ'])

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

def calc(model):
    res = 0
    for col in model.keys():
        res += model.get(col)
    return healthy(res[0])

diagnose1 = calc(df_model1)
diagnose2 = calc(df_model2)
diagnose3 = calc(df_model3)
diagnose4 = calc(df_model4)

st.subheader("Полученные результаты")
results = st.container()

with results:
    c1,c2,c3,c4,c5,c6,c7,c8 = st.columns([3,3,3,3,3,3,3,3])
    with c1:
        "**Модель 1:**"
    with c2:
        st.write(diagnose1)
    with c3:
        "**Модель 2:**"
    with c4:
        st.write(diagnose2)
    with c5:
        "**Модель 3:**"
    with c6:
        st.write(diagnose3)
    with c7:
        "**Модель 4:**"
    with c8:
        st.write(diagnose4)

state.update()


