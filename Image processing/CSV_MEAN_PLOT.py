import pandas as pd 
import matplotlib.pyplot as plt 
sample_data= pd.read_csv('excel.csv')
print(sample_data)
sample_data.head()
sum_freq=sum(sample_data['fraq'])
sum_score=sum(sample_data['fraqxscore'])
mean=0.0
mean=float(sum_score/sum_freq)
print(float(mean))
plt.figure(0)
ax=plt.subplot()
ax.set_xlable('sample_data')
ax.plot(sample_data['fraq'])
ax.plot(sample_data['fraqxscore'])
plt.show()
