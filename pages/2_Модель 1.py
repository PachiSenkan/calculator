import streamlit as st
import pandas as pd
from streamlit import session_state as state
from Главная import healthy
from pages.neuralModels import load_model_file
from pages.neuralModels import getFeaturesFromModel
from pages.neuralModels import getValuesForModel
from pages.neuralModels import FileList

st.set_page_config(page_title='Калькулятор ХВЗК')

if state.keys():
    st.header("Диагностическая модель 1")
    st.subheader("Тип модели: Случайный лес")
    st.subheader("Введенные показатели")
    if 'FIO' in state:
        state['FIO']
    clf = load_model_file(FileList[0])
    listOfFeatures = getFeaturesFromModel(clf)
    dictOfSliderVal = {
    'гемоглобин':137.,
    'гематокрит':44.,
    'mcv':83.,'соэ':6.,
    'ферритин':81.,
    'кальпротектин':43.,
    'e c-цис (c-c18:1)':9.011,
    'e t-транс (t-c18:1)':1.298,
    'e 7,10,13,16-c22:4':2.263,
    'e 5,8,11,14-c20:4':9.985,
    'e полиненасыщ':26.087,
    's 7,10,13,16-c22:4':.151,
    's омега-3':1.905,
    's 5,8,11,14-c20:4':4.706,
    's омега-6/омега-3':12.999,
    's полиненасыщ':26.694,
    }
    for v in dictOfSliderVal:
        if v in state:
            state[v] = dictOfSliderVal[v]
    #dictOfSliderVal
    dictOfValForModel = getValuesForModel(clf)
    df_forModel = pd.DataFrame.from_dict(dictOfValForModel,orient='index').T # , 'columns' 'index', 'tight'
    
    df_forModel
    targetClasesName = ['Здоров','Болен']
    
    y_probability = clf.predict_proba(df_forModel.values)[0]
    
    y_fullAnswer = clf.predict(df_forModel.values)
    y_numOfClass = int( y_fullAnswer[0][0])

    st.subheader("Предлагаемый диагноз")

    for tclass, prob in zip( targetClasesName, y_probability):
        st.write(f'{tclass:>6}: {prob:.1%}')

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