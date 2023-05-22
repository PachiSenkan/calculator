import streamlit as st
from neuralModels import calculateDiagnoseDisease
from neuralModels import calculateDiagnoseForm

from streamlit import session_state as state

st.set_page_config(page_title='Калькулятор ХВЗК', layout='wide')

st.markdown("""
<style>
.stNumberInput
{
    display: flex;
    justify-content: space-between;
}
.css-k1ih3n {
    width: 100%;
    padding: 1rem 5rem 10rem;
    min-width: auto;
    max-width: initial;
}

</style>
""", unsafe_allow_html=True)

st.header("Диагностический калькулятор для оценки формы и стадии воспалительных заболеваний кишечника", )
st.subheader("Введите необходимые показатели")
if 'FIO' in state:
    state['FIO']

for key in state.keys():
    if key != 'uploaded':
        state[key] = state[key]
state.update()

#Создание вкладок ввода данных
tab1, tab2, tab3 = st.tabs(["Основные показатели", "Кислоты 1", "Кислоты 2"])

with tab1:
    #На вкладке 1 создаем 2 колонки
    tab1_col1, tab1_col2 = st.columns(2)
    #В каждой колонке располагаем элементы ввода
    with tab1_col1:
        st.number_input("Гемоглобин",0.0, 200.0, key = "гемоглобин")
        st.number_input("MCHC", 0.0, 1000.0, key = "mchc")
        st.number_input("Лейкоциты", 0.0, 100.0, key = "лейкоциты")
        st.number_input("Гематокрит", 0.0, 100.0, key = "гематокрит")
        st.number_input("СОЭ", 0.0, 100.0, key = "соэ")
        st.number_input("Кальпротектин", 0.0, 1000.0, key = "кальпротектин")
    with tab1_col2:
        st.number_input("MCV", 0.0, 100.0, key = "mcv")
        st.number_input("СРБ", 0.0, 100.0, key = "срб")
        st.number_input("Фибриноген", 0.0, 100.0, key = "фибриноген")
        st.number_input("MCH", 0.0, 100.0, key = "mch")
        st.number_input("Ферритин", 0.0, 100.0, key = "ферритин")

with tab2:
    tab2_col1, tab2_col2 = st.columns(2)
    with tab2_col1:
        st.number_input("e c-цис (c-c18:1)", 0.0, 100.0, key="e c-цис (c-c18:1)")
        st.number_input("e 7,10,13,16-c22:4", 0.0, 100.0, key="e 7,10,13,16-c22:4")
        st.number_input("e 11,14-c20:2", 0.0, 100.0, key="e 11,14-c20:2")
        st.number_input("e 5,8,11,14-c20:4", 0.0, 100.0, key="e 5,8,11,14-c20:4")
    with tab2_col2:
        st.number_input("e t-транс (t-c18:1)", 0.0, 100.0, key="e t-транс (t-c18:1)")
        st.number_input("e полиненасыщ", 0.0, 100.0, key = "e полиненасыщ")
        st.number_input("e c12:0", 0.0, 100.0, key = "e c12:0")

with tab3:
    tab3_col1, tab3_col2 = st.columns(2)
    with tab3_col1:
        st.number_input("s 7,10,13,16-c22:4", 0.0, 10.0, key="s 7,10,13,16-c22:4")
        st.number_input("s 5,8,11,14,17-c20:5", 0.0, 100.0, key="s 5,8,11,14,17-c20:5")
        st.number_input("s 5,8,11,14-c20:4", 0.0, 100.0, key="s 5,8,11,14-c20:4")
        st.number_input("s c12:0", 0.0, 100.0, key="s c12:0")
    with tab3_col2:
        st.number_input("s омега-3", 0.0, 100.0, key="s омега-3")
        st.number_input("s омега-3/омега-6", 0.0, 100.0, key="s омега-6/омега-3")
        st.number_input("s полиненасыщ", 0.0, 100.0, key = "s полиненасыщ")

st.subheader("Полученные результаты")
results = st.container()

with results:
    c1,c2,c3,c4,c5, = st.columns([3,3,3,3,3])
    with c1:
        "**Модель 1:**"
        result = calculateDiagnoseDisease(0, False)
        if result:
            for tclass, prob in result:
                st.write(f'{tclass: >6}: {prob:.1%}')
    with c2:
        "**Модель 2:**"
        result = (calculateDiagnoseDisease(1, False))
        if result:
            for tclass, prob in result:
                st.write(f'{tclass: >6}: {prob:.1%}')
    with c3:
        "**Модель 3:**"
        result = (calculateDiagnoseDisease(2, False))
        if result:
            for tclass, prob in result:
                st.write(f'{tclass: >6}: {prob:.1%}')
    with c4:
        "**Модель 4:**"
        result = (calculateDiagnoseForm(3, False))
        if result:
            for tclass, prob in result:
                st.write(f'{tclass: >6}: {prob:.1%}')
    with c5:
        "**Модель 5:**"
        result = (calculateDiagnoseForm(4, False))
        if result:
            for tclass, prob in result:
                st.write(f'{tclass: >6}: {prob:.1%}')

state.update()


