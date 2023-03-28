import streamlit as st
import pandas as pd
from streamlit import session_state as state
st.set_page_config(page_title='Калькулятор ХВЗК')
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
    df_model3 = pd.DataFrame([[state.ampl_def_state, state.soe_state, state.eritr_speed_state]],
                            columns=['Ампл деф на 1мгц', 'СОЭ', 'Скорость движения эритроцитов'])
    
    st.header("Диагностическая модель 3")
    st.subheader("Введенные показатели")
    if 'FIO' in state:
        state['FIO']
    df_model3
    st.subheader("Полученное значение")
    res = 0
    for col in df_model3.keys():
      res += df_model3.get(col)
    diagnose1 = healthy(res[0])
    st.write(res)
    st.subheader("Предлагаемый диагноз")
    st.write(diagnose1)
    if 'uploaded_params' in state:
        st.subheader("Все данные пациента")
        state['uploaded_patient']
    
    for key in state.keys():
        if key != 'uploaded':
            state[key] = state[key]
    state.update()