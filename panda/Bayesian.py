
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#now laod the csvdata file using the pandas read_csv method
play_tennis=pd.read_csv("Playtennis.csv")
print(play_tennis.head())
#in this example we use the python

number=LabelEncoder()
play_tennis['Outlook']=number.fit_transform(play_tennis['Outlook'])
play_tennis['Temperature']=number.fit_transform(play_tennis['Temperature'])
play_tennis['Humidity']=number.fit_transform(play_tennis['Humidity'])
play_tennis['Wind']=number.fit_transform(play_tennis['Wind'])
play_tennis['Play Tennis']=number.fit_transform(play_tennis['Play Tennis'])
features=['Outlook','Temperature','Humidity','Wind']
print(play_tennis)
target="Play Tennis"

features_train,features_test,target_train,target_test=train_test_split(play_tennis[features],play_tennis[target],test_size=0.33,random_state=54)
model=GaussianNB()
model.fit(features_train,target_train)
pred=model.predict(features_test)
accuracy=accuracy_score(target_test,pred)
print(accuracy*100)
pred1=model.predict([[1,2,0,1]])
print(pred1)
