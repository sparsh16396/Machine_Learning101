import pandas as pd 
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
play_tennis=pd.read_csv("/home/abes/Desktop/PlayTennis.csv")
print(play_tennis.head())
number = LabelEncoder()
play_tennis['Outlook']=number.fit_transform(play_tennis['Outlook'])
play_tennis['Temperature']=number.fit_transform(play_tennis['Temperature'])
play_tennis['Humidity']=number.fit_transform(play_tennis['Humidity'])
play_tennis['Wind']=number.fit_transform(play_tennis['Wind'])
play_tennis['Play Tennis']=number.fit_transform(play_tennis['Play Tennis'])
#play_tennis['Outlook']=number.fit_transform(play_tennis['Outlook'])
features=['Outlook','Temperature','Humidity','Wind']
print(play_tennis)
target= 'Play Tennis'
features_train,features_test,target_train,target_test=train_test_split(play_tennis[features], play_tennis[target],test_size=0.30, random_state=54)
#model=svm.SVC(kernel='linear')
#models= svm.SVC()
k_value=5 
model= KNeighborsClassifier(n_neighbors = k_value)
model.fit(features_train, target_train)
pred=model.predict(features_test)
accuracy = accuracy_score(target_test,pred)
print(accuracy*100)
pred1=model.predict([[1,2,0,1]])
print(pred1)
