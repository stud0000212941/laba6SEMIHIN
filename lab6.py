import streamlit as st
import pandas as pd
df = pd.read_csv('data.csv')
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
  user_input_class = st.text_input("Введите класс пасажира "1, 2 или 3" >>: ")
  user_input_sex = st.text_input("Пол пасажира "male или female>>: ")
  sik =df[(df['Pclass']==user_input_class) & (df['Sex']==user_input_sex) & (df['Survived']==1)][["Name","Sex","Age"]]
  st.dataframe(sik)
if option == 'задача 2)':
  option_2 = st.selectbox(
    'Выберете',
    ('спасен', 'нет'))
  df[(df["Fare"]==0.0) & (df['Survived']==searched_survived)]
  st.dataframe(spas)
else: st.write(
    "#Выберете задачу"
)
