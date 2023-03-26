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

state = st.session_state
df_model2 = pd.DataFrame([[state.hematokrit_state, state.discocyte_state, state.s_t_18_1_state]],
                        columns=['Гематокрит', 'Доля дискоцитов', 's t-c18:1'])

st.header("Диагностическая модель 2")
st.subheader("Введенные показатели")
df_model2
st.subheader("Полученное значение")
res2 = 0
for col in df_model2.keys():
    res2 += df_model2.get(col)
diagnose2 = healthy(res2[0])
st.write(res2)
st.subheader("Предлагаемый диагноз")
st.write(diagnose2)

for key in state.keys():
  state[key] = state[key]
state.update()