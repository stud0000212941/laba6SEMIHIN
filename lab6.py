import streamlit as st
import pandas as pd
df = pd.read_csv('data.csv')
def funk1(user_input_class,user_input_sex,df):
    sik =df[(df['Pclass']==user_input_class) & (df['Sex']==user_input_sex) & (df['Survived']==1)][["Name","Sex","Age"]]
    return sik
def funk2(searched_survived,df):
    spas=df[(df["Fare"]==0.0) & (df['Survived']==searched_survived)]
    return spas
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
  user_input_class = st.selectbox(
    'класс пасажира',
    (1, 2, 3))
  user_input_sex = st.selectbox(
    'Пол пасажира',
    ('male', 'female'))
  sik=funk1(user_input_class,user_input_sex,df)
  st.dataframe(sik)
if option == 'задача 2)':
  option_2 = st.selectbox(
    'Выберете',
    ('спасен', 'нет'))
  if option_2 == 'спасен':
      searched_survived = 1
  else:
      searched_survived = 0
  spas=funk2(searched_survived,df)
  st.dataframe(spas)
else: st.write(
    "#Выберете задачу"
)
