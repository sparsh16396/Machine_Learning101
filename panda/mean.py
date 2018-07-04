import pandas as pd 
import matplotlib.pyplot as plt 
sd=pd.read_csv('C:/Users/SHRAMA JEE/Documents/mean_python.csv',)
print(sd)
sd.head()
sum_freq=sum(sd['f'])
sum_score=sum(sd['fxs'])
mean=sum_score/sum_freq
print(mean)
plt.figure(0)
ax=plt.subplot()
ax.set_xlabel('sd')
ax.plot(sd['f'])
ax.plot(sd['fxs'])
plt.show()
