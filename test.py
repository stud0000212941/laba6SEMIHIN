import pandas as pd
from io import StringIO
import lab6.py as funk2          
def test_funk2():
  csv_string = """PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
  7,0,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S
  270,1,1,"Bissette, Miss. Amelia",female,35,0,0,PC 17760,135.6333,C99,S
  271,0,1,"Cairns, Mr. Alexander",male,,0,0,113798,31,,S
  272,1,3,"Tornquist, Mr. William Henry",male,25,0,0,LINE,0,,S
  273,1,2,"Mellinger, Mrs. (Elizabeth Anne Maidment)",female,41,0,1,250644,19.5,,S
  """
  df = pd.read_csv(StringIO(csv_string), sep=",")
  searched_survived = 1
  spas = funk2(searched_survived,df)
  assert len(spas) == 1
