import streamlit as st
import pandas as pd
import io
import copy
from streamlit import session_state as state
from neuralModels import calculateDiagnoseFormFile
from neuralModels import calculateDiagnoseDiseaseFile

st.header("Диагностический калькулятор для оценки формы и стадии воспалительных заболеваний кишечника")

st.subheader("Выберите файл для загрузки")

uploaded_file = st.file_uploader("Загрузка файла", label_visibility="hidden", type='xlsx')

@st.experimental_singleton
def convert_df(df):
    return df.to_excel("Результаты.xlsx")

if state.keys():
    ""

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
    patient = st.container()
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
    with patient:
        st.dataframe(state['uploaded_patient'])

if 'uploaded_table' in state:
    st.subheader("Загруженные данные")
    st.dataframe(state['uploaded_table'])
    if st.button('Провести анализ всех пациентов из файла'):
        out_table = copy.deepcopy(state['uploaded_table'])
        out_table.insert(1,"Модель 1", None)
        out_table.insert(2, "Модель 2", None)
        out_table.insert(3, "Модель 3", None)
        out_table.insert(4, "Модель 4", None)
        out_table.insert(5, "Модель 5", None)
        for i in range(1,len(state['uploaded_table'].index)+1):

            if i == 0:
                patient = state['uploaded_table'].iloc[:1]
            else:
                patient = state['uploaded_table'].iloc[i-1:i]
            #st.write(patient['гемоглобин'])
            answer1 = calculateDiagnoseDiseaseFile(0, patient)
            answer2 = calculateDiagnoseDiseaseFile(1,patient)
            answer3 = calculateDiagnoseDiseaseFile(2,patient)
            answer4 = calculateDiagnoseFormFile(3, patient)
            answer5 = calculateDiagnoseFormFile(4, patient)

            out1 = ''
            out2 = ''
            out3 = ''
            out4 = ''
            out5 = ''
            for tclass, prob in answer1:
                out1 += (f'{tclass: >6}: {prob:.1%}')
                out1 += '\n'
            out_table.at[i-1, 'Модель 1'] = out1
            for tclass, prob in answer2:
                out2 += (f'{tclass: >6}: {prob:.1%}')
                out2 += '\n'
            out_table.at[i - 1, 'Модель 2'] = out2
            for tclass, prob in answer3:
                out3 += (f'{tclass: >6}: {prob:.1%}')
                out3 += '\n'
            out_table.at[i-1, 'Модель 3'] = out3
            for tclass, prob in answer4:
                out4 += (f'{tclass: >6}: {prob:.1%}')
                out4 += '\n'
            out_table.at[i-1, 'Модель 4'] = out4
            for tclass, prob in answer5:
                out5 += (f'{tclass: >6}: {prob:.1%}')
                out5 += '\n'
            out_table.at[i-1, 'Модель 5'] = out5

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


# upload(uploaded_file)

for key in state.keys():
    if key != 'uploaded':
        state[key] = state[key]
# state
state.update()
