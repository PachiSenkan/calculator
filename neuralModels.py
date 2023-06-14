import sys
import numpy as np
import sklearn 
import pandas as pd
import Orange # https://orange3.readthedocs.io/en/latest/
import streamlit as st
import pickle
import json
from streamlit import session_state as state

@st.cache_resource
def load_model_file(fileName):
    with open(fileName, 'rb') as filestream:
        clf = pickle.load(filestream)
    return clf

def getFeaturesFromModel(model):
    listOfFeatures = []

    for ind, __ in enumerate(model.domain.attributes):
        listOfFeatures.append(model.domain.attributes[ind].name)
    return listOfFeatures

def getValuesForModel(model):
    listOfFeatures = getFeaturesFromModel(model)
    dictOfValForModel = {}
    with st.expander("Введите недостающие показатели"):
        for colName in listOfFeatures:
            #st.write(colName, end='')
            if colName in state and state[colName] != 0:
                dictOfValForModel[colName] = state[colName]
            else:
                st.warning(f'{colName}')
                state['Exception'] = True
    return dictOfValForModel

def getValuesForModelFile(model, patient):
    # st.write('Формирование значений признаков для конкретной модели')

    listOfFeatures = getFeaturesFromModel(model)

    dictOfValForModel = {}
    with st.expander("Введите недостающие показатели"):
        for colName in listOfFeatures:

            if colName in patient:

                dictOfValForModel[colName] = patient[colName]
            #else:
                #st.warning(f'Введите:{colName}')
                #state['Exception'] = True
    return dictOfValForModel

FileList = [
    r'models/ХВЗК Здоровые-Больные LogisticReg_L1_C=0. vPub.pkcls',
    r'models/ХВЗК Здоровые-Больные Дерево5 X-Свой4. vPub.pkcls',
    r'models/ХВЗК Здоровые-Больные LogisticReg_L1_C=0. vPub.pkcls',
    r'models/ХВЗК НЯК-НКК Дерево5 X-Свой4. vPub.pkcls',
    r'models/ХВЗК НЯК-НКК LogisticReg_L1_C=0. vPub.pkcls',
]


def calculateDiagnoseDisease(num, print):
    clf = load_model_file(FileList[num])
    dictOfValForModel = getValuesForModel(clf)
    if state['Exception'] == False:
        df_forModel = pd.DataFrame.from_dict(dictOfValForModel, orient='index', dtype=np.float64).T  # , 'columns' 'index', 'tight'
        if print:
            st.dataframe(df_forModel)
        targetClasesName = ['Здоров', 'Болен']
        y_probability = clf.predict_proba(df_forModel.values)[0]
        return zip(targetClasesName, y_probability)
    else:
        state['Exception'] = False


def calculateDiagnoseForm(num, print):
    clf = load_model_file(FileList[num])
    dictOfValForModel = getValuesForModel(clf)
    if state['Exception'] == False:
        df_forModel = pd.DataFrame.from_dict(dictOfValForModel, orient='index', dtype=np.float64).T  # , 'columns' 'index', 'tight'
        if print:
            st.dataframe(df_forModel)
        targetClasesName = ['НЯК', 'НКК']

        y_probability = clf.predict_proba(df_forModel.values)[0]
        return zip(targetClasesName, y_probability)
    else:
        state['Exception'] = False


def calculateDiagnoseDiseaseFile(num, patient):

    clf = load_model_file(FileList[num])
    dictOfValForModel = getValuesForModelFile(clf, patient)
    df_forModel = pd.DataFrame.from_dict(dictOfValForModel, dtype=np.float64)  # , 'columns' 'index', 'tight'
    targetClasesName = ['Здоров', 'Болен']
    y_probability = clf.predict_proba(df_forModel.values)[0]
    return zip(targetClasesName, y_probability)

def calculateDiagnoseFormFile(num, patient):
    clf = load_model_file(FileList[num])
    dictOfValForModel = getValuesForModelFile(clf, patient)

    df_forModel = pd.DataFrame.from_dict(dictOfValForModel, dtype=np.float64)  # , 'columns' 'index', 'tight'
    targetClasesName = ['НЯК', 'НКК']

    y_probability = clf.predict_proba(df_forModel.values)[0]

    return zip(targetClasesName, y_probability)


#def calculateDiagnoseDisease(num, dict, print):
#    clf = load_model_file(FileList[num])
#    if dict != None:
#        for v in dict:
#            if v in state:
#                state[v] = dict[v]
#    dictOfValForModel = getValuesForModel(clf)
#    if state['Exception'] == False:
#
#        df_forModel = pd.DataFrame.from_dict(dictOfValForModel, orient='index', dtype=np.float64).T  # , 'columns' 'index', 'tight'
#        if print:
#            st.dataframe(df_forModel)
#
#        targetClasesName = ['Здоров', 'Болен']
#
#        y_probability = clf.predict_proba(df_forModel.values)[0]
#        y_fullAnswer = clf.predict(df_forModel.values)
#        y_numOfClass = int(y_fullAnswer[0][0])
#        return zip(targetClasesName, y_probability)
#    else:
#        state['Exception'] = False
#
#
#def calculateDiagnoseForm(num, dict, print):
#    clf = load_model_file(FileList[num])
#
#    if dict != None:
#        for v in dict:
#            if v in state:
#                state[v] = dict[v]
#    dictOfValForModel = getValuesForModel(clf)
#    if state['Exception'] == False:
#        df_forModel = pd.DataFrame.from_dict(dictOfValForModel, orient='index', dtype=np.float64).T  # , 'columns' 'index', 'tight'
#        if print:
#            st.dataframe(df_forModel)
#        targetClasesName = ['НЯК', 'НКК']
#
#        y_probability = clf.predict_proba(df_forModel.values)[0]
#        return zip(targetClasesName, y_probability)
#    else:
#        state['Exception'] = False
