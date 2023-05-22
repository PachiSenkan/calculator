import streamlit as st
from streamlit import session_state as state
from neuralModels import calculateDiagnoseDisease

st.set_page_config(page_title='Калькулятор ХВЗК')

if state.keys():
    st.header("Диагностическая модель 1")
    st.subheader("Тип модели: Случайный лес")
    st.subheader("Введенные показатели")
    if 'FIO' in state:
        state['FIO']

    state['Exception'] = False
    result = calculateDiagnoseDisease(0, True)
    if result:
        st.subheader("Предлагаемый диагноз")
        for tclass, prob in result:
            st.write(f'{tclass: >6}: {prob:.1%}')

    if 'uploaded_params' in state:
        st.subheader("Все данные пациента")
        state['uploaded_patient']

    for key in state.keys():
        if key != 'uploaded':
            state[key] = state[key]
    state.update()

else:
    st.header("Диагностическая модель 1")
    st.subheader("Вернитесь на главную страницу")