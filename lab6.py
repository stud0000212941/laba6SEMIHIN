import streamlit as st
import requests

st.title(
    "#Веб-приложение для обработки данных пассажиров “Титаника”"
)
st.write(
    "#задача 1) Name, Sex, Age спасенных пассажиров указанного класса и пола."
"#задача 2)  данные пассажиров с билетом нулевой стоимости, выбрав спасен/нет."
)
# user_input = st.text_input("Выберете задачу >>: ")
option = st.selectbox(
    'Выберете задачу',
    ('задача 1)', 'задача 2)'))
if option == 'задача 1)':
  user_input_class = st.text_input("Введите класс пасажира >>: ")
  user_input_sex = st.text_input("Пол пасажира >>: ")
  st.dataframe(sik)
if option == 'задача 2)':
  option_2 = st.selectbox(
    'Выберете',
    ('спасен', 'нет'))
  st.dataframe(spas)
else: st.write(
    "#Выберете задачу"
)
