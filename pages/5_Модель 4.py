import streamlit as st
import pandas as pd
from streamlit import session_state as state
from pages.neuralModels import load_model_file
from pages.neuralModels import getFeaturesFromModel
from pages.neuralModels import getValuesForModel
from pages.neuralModels import calculateDiagnoseForm
from pages.neuralModels import FileList
st.set_page_config(page_title='Калькулятор ХВЗК')

if state.keys():
    st.header("Диагностическая модель 4")
    st.subheader("Тип модели: Дерево")
    st.subheader("Введенные показатели")
    if 'FIO' in state:
        state['FIO']
    #clf = load_model_file(FileList[3])
    #listOfFeatures = getFeaturesFromModel(clf)
    dictOfSliderVal = {
        'гемоглобин': 110.,
        'гематокрит': 36.,
        'mcv': 80.,
        'mch': 27.,
        'mchc': 308.,
        'соэ': 27.,
        'срб': 13.,
        'ферритин': 11.,
        'лейкоциты': 9.,
        'e c-цис (c-c18:1)': 10.485,
        'e 7,10,13,16-c22:4': 1.626,
        'e 11,14-c20:2': .257,
        'e c12:0': .05,
        's 7,10,13,16-c22:4': .147,
        's 5,8,11,14,17-c20:5': .37,
        's c12:0': .014,
        'кальпротектин': 234.,
        'фибриноген': 6.,
    }
    state['Exception'] = False
    result = calculateDiagnoseForm(3, None, True)
    if result:
        st.subheader("Предлагаемый диагноз")
        for tclass, prob in result:
            st.write(f'{tclass: >6}: {prob:.1%}')
    #for v in dictOfSliderVal:
    #    if v in state:
    #        state[v] = dictOfSliderVal[v]
    ## dictOfSliderVal
    #dictOfValForModel = getValuesForModel(clf)
    #df_forModel = pd.DataFrame.from_dict(dictOfValForModel, orient='index').T  # , 'columns' 'index', 'tight'
    #df_forModel
    #
    #targetClasesName = ['НЯК', 'НКК']
    #
    #y_probability = clf.predict_proba(df_forModel.values)[0]
    #
    #y_fullAnswer = clf.predict(df_forModel.values)
    #y_numOfClass = int(y_fullAnswer[0][0])
    #
    #st.subheader("Предлагаемый диагноз")
    #
    #for tclass, prob in zip(targetClasesName, y_probability):
    #    st.write(f'{tclass:>6}: {prob:.1%}')

    if 'uploaded_params' in state:
        st.subheader("Все данные пациента")
        state['uploaded_patient']

    for key in state.keys():
        if key != 'uploaded':
            state[key] = state[key]
    state.update()

else:
    st.header("Диагностическая модель 4")
    st.subheader("Вернитесь на главную страницу")