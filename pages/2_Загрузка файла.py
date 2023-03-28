import time
import streamlit as st
import pandas as pd
import numpy as np
import random
import openpyxl
import io
from streamlit import cache
from streamlit import session_state as state

st.header("Диагностический калькулятор для оценки формы и стадии воспалительных заболеваний кишечника")

st.subheader("Выберите файл для загрузки")

uploaded_file = st.file_uploader("Загрузка файла", label_visibility="hidden")


# if uploaded_file is not None:
#    params = pd.read_excel(uploaded_file, sheet_name='params')
#    pars = params.columns.ravel().tolist()
#    sheet = pd.read_excel(uploaded_file, sheet_name='main')
#    st.subheader("Загруженные данные")
#    #sheet
#    i = 0
#    for par in pars:
#        # if par != 'FIO':
#        state[par] = sheet.iloc[0, i]
#        i += 1
# state
# @st.experimental_memo()
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_excel("Результаты.xlsx")

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
if state.keys():
    ""
    #df_model1 = pd.DataFrame([[state['hemoglobin_state'], state.mcv_state, state.e_cis_18_1_state]],
    #                        columns=['Гемоглобин', 'MCV', 'e c-цис (c-c18:1)'])
    #df_model2 = pd.DataFrame([[state.hematokrit_state, state.discocyte_state, state.s_t_18_1_state]],
    #                        columns=['Гематокрит', 'Доля дискоцитов', 's t-c18:1'])
    #df_model3 = pd.DataFrame([[state.ampl_def_state, state.soe_state, state.eritr_speed_state]],
    #                        columns=['Ампл деф на 1мгц', 'СОЭ', 'Скорость движения эритроцитов'])
    #df_model4 = pd.DataFrame([[state.s_20_5_state, state.s_omega_3_6_state, state.s_poly_state]],
    #                        columns=['s 5,8,11,14,17-c20:5', 's омега-3/омега-6', 's полиненасыщ'])

def upload():
    params = pd.read_excel(uploaded_file, sheet_name='params')
    pars = params.columns.ravel().tolist()
    state['uploaded_params'] = pars
    sheet = pd.read_excel(uploaded_file, sheet_name='main')
    state['uploaded_table'] = sheet
    #if 'uploaded_counter' not in state:
    state['uploaded_counter'] = 1
    current_patient = sheet.iloc[state['uploaded_counter']-1:state['uploaded_counter']]
    state['uploaded_patient'] = current_patient

if uploaded_file is not None:
    upload()

if 'uploaded_patient' in state:
    st.subheader('Исследуемый пациент')

    if st.button('Следующий пациент'):
        if state['uploaded_counter'] < len(state['uploaded_table'].index):
            state['uploaded_counter'] += 1
            state['uploaded_patient'] = state['uploaded_table'].iloc[state['uploaded_counter']-1:state['uploaded_counter']]
        else:
            state['uploaded_counter'] = 1
            state['uploaded_patient'] = state['uploaded_table'].iloc[state['uploaded_counter'] - 1:state['uploaded_counter']]
    if 'uploaded_params' in state:
        i = 0
        for par in state['uploaded_params']:
            # if par != 'FIO':
            state[par] = state['uploaded_table'].iloc[state['uploaded_counter']-1,i]
            i += 1
    st.dataframe(state['uploaded_patient'])

if 'uploaded_table' in state:
    st.subheader("Загруженные данные")
    st.dataframe(state['uploaded_table'])
    if st.button('Провести анализ всех пациентов из файла'):
        out_table = state['uploaded_table']
        out_table.insert(1,"Модель 1", None)
        out_table.insert(2, "Модель 2", None)
        out_table.insert(3, "Модель 3", None)
        out_table.insert(4, "Модель 4", None)
        for i in range(1,len(state['uploaded_table'].index)+1):
            if i == 0:
                patient = state['uploaded_table'].iloc[:1]
            else:
                patient = state['uploaded_table'].iloc[i-1:i]
            df_model1 = pd.DataFrame([[patient['Гемоглобин'], patient['MCV'], patient['e c-цис (c-c18:1)']]],
                                     columns=['Гемоглобин', 'MCV', 'e c-цис (c-c18:1)'])
            res1 = 0
            for col in range(len(df_model1.columns)):
                res1 += df_model1.iloc[0,col]
            diagnose1 = healthy(res1.iloc[0])

            df_model2 = pd.DataFrame([[patient['Гематокрит'], patient['Доля дискоцитов'], patient['s t-c18:1']]],
                                     columns=['Гематокрит', 'Доля дискоцитов', 's t-c18:1'])
            res2 = 0
            for col in range(len(df_model2.columns)):
                res2 += df_model2.iloc[0,col]
            diagnose2 = healthy(res2.iloc[0])

            df_model3 = pd.DataFrame([[patient['Ампл деф на 1 МГц'], patient['СОЭ'], patient['Скорость движения эритроцитов']]],
                                     columns=['Ампл деф на 1мгц', 'СОЭ', 'Скорость движения эритроцитов'])
            res3 = 0
            for col in range(len(df_model3.columns)):
                res3 += df_model3.iloc[0,col]
            diagnose3 = healthy(res3.iloc[0])

            df_model4 = pd.DataFrame([[patient['s 5,8,11,14,17-c20:5'], patient['s омега-3/омега-6'], patient['s полиненасыщ']]],
                                     columns=['s 5,8,11,14,17-c20:5', 's омега-3/омега-6', 's полиненасыщ'])
            res4 = 0
            for col in range(len(df_model4.columns)):
                res4 += df_model4.iloc[0,col]
            diagnose4 = healthy(res4.iloc[0])
            out_table.at[i-1, 'Модель 1'] = diagnose1
            out_table.at[i-1, 'Модель 2'] = diagnose2
            out_table.at[i-1, 'Модель 3'] = diagnose3
            out_table.at[i-1, 'Модель 4'] = diagnose4

        out_table
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            out_table.to_excel(writer, index=False)
            writer.save()
            download = st.download_button(
                label="Скачать файл результатов",
                data=buffer,
                file_name='Результаты.xlsx',
                mime='application/vnd.ms-excel'
            )
        #out_file = convert_df(out_table)
        #st.download_button(
        #    label="Скачать файл результатов",
        #    file_name='large_df.csv'
        #)


# upload(uploaded_file)

for key in state.keys():
    if key != 'uploaded':
        state[key] = state[key]
# state
state.update()
