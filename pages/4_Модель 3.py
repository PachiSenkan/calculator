import streamlit as st
from streamlit import session_state as state
from neuralModels import calculateDiagnoseDisease

st.set_page_config(page_title='Калькулятор ХВЗК')

if state.keys():
    st.header("Диагностическая модель 3")
    st.subheader("Тип модели: Логистическая регрессия")
    st.subheader("Введенные показатели")
    if 'FIO' in state:
        state['FIO']

    dictOfSliderVal = {
        'гемоглобин': 137.,
        'гематокрит': 44.,
        'mcv': 83., 'соэ': 6.,
        'ферритин': 81.,
        'кальпротектин': 43.,
        'e c-цис (c-c18:1)': 9.011,
        'e t-транс (t-c18:1)': 1.298,
        'e 7,10,13,16-c22:4': 2.263,
        'e 5,8,11,14-c20:4': 9.985,
        'e полиненасыщ': 26.087,
        's 7,10,13,16-c22:4': .151,
        's омега-3': 1.905,
        's 5,8,11,14-c20:4': 4.706,
        's омега-6/омега-3': 12.999,
        's полиненасыщ': 26.694,
    }
    state['Exception'] = False
    result = calculateDiagnoseDisease(2, True)

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
    st.header("Диагностическая модель 3")
    st.subheader("Вернитесь на главную страницу")