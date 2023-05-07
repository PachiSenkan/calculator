import sys
import numpy as np
import sklearn 
import pandas as pd
import Orange # https://orange3.readthedocs.io/en/latest/
import streamlit as st
import pickle
import json
from streamlit import session_state as state

@st.experimental_singleton
def load_model_file(fileName):
    #st.write('Открыт: ', fileName)
    with open(fileName, 'rb') as filestream:
        clf = pickle.load(filestream)

    #st.write(clf.__class__)
    #st.write(clf.name)  # Имя из Orange
    #st.write(clf.domain)
    return clf

def getFeaturesFromModel(model):
    #st.write('Получить список и очерёдность исков для контретной модели')

    # создать пустой список
    listOfFeatures = []

    # обойти список model.domain.attributes, который хранит используемые признаки
    for ind, __ in enumerate(model.domain.attributes):
        # копировать имя признака
        listOfFeatures.append(model.domain.attributes[ind].name)
    return listOfFeatures

def getValuesForModel(model):
    #st.write('Формирование значений признаков для конкретной модели')

    listOfFeatures = getFeaturesFromModel(model)

    dictOfValForModel = {}
    for colName in listOfFeatures:
        #st.write(colName, end='')
        if colName in state and state[colName] != 0:
            #st.write(f' ...Найден, значение: {dictOfSliderVal[colName]}')
            dictOfValForModel[colName] = state[colName]
        else:
            st.warning(f'Введите значение:{colName}')
    return dictOfValForModel

FileList = [
    r'C:\Users\Pachi\PycharmProjects\dip\models\ХВЗК Здоровые-Больные СлучайныйЛес 5деревъев 5глубина X-Свой4. vPub.pkcls',
    r'C:\Users\Pachi\PycharmProjects\dip\models\ХВЗК Здоровые-Больные Дерево5 X-Свой4. vPub.pkcls',
    r'C:\Users\Pachi\PycharmProjects\dip\models\ХВЗК Здоровые-Больные LogisticReg_L1_C=0. vPub.pkcls',
    r'C:\Users\Pachi\PycharmProjects\dip\models\ХВЗК НЯК-НКК Дерево5 X-Свой4. vPub.pkcls',
    r'C:\Users\Pachi\PycharmProjects\dip\models\ХВЗК НЯК-НКК LogisticReg_L1_C=0. vPub.pkcls',
]
fileName = FileList[0]
clf = load_model_file(fileName)
listOfFeatures = getFeaturesFromModel(clf)
listOfFeatures

dictOfSliderVal = {
'гемоглобин':129.,
'гематокрит':37.,
'mcv':86.,
'соэ':10.,
'ферритин':100.,
'кальпротектин':48.,
'e c-цис (c-c18:1)':14.46,
'e t-транс (t-c18:1)':1.67,
'e 7,10,13,16-c22:4':2.36,
'e 5,8,11,14-c20:4':15.8,
'e полиненасыщ':42.29,
's 7,10,13,16-c22:4':.16,
's омега-3':2.43,
's 5,8,11,14-c20:4':2.91,
's омега-6/омега-3':13.36,
's полиненасыщ':34.9,
}

dictOfSliderVal
dictOfValForModel = getValuesForModel(clf)

#df_forModel = pd.DataFrame.from_dict(dictOfValForModel,orient='index').T # , 'columns' 'index', 'tight'
#df_forModel

st.write("Вывести названия и порядок классов")
#targetClasesName = clf.domain.class_var.values
#targetClasesName

st.write("Вычислить вероятности=степени уверенности")
#st.write(clf.name)
#y_probability = clf.predict_proba(df_forModel.values)[0]
#y_probability

st.write("Вероятность отнесения к классам")
#st.write(clf.name)
#for tclass, prob in zip( targetClasesName, y_probability):
#    st.write(f'{tclass:>6}: {prob:.1%}')
#
#y_fullAnswer = clf.predict(df_forModel.values)
#y_numOfClass = int( y_fullAnswer[0][0])
#clf.domain.class_var.values[int(y_numOfClass)]