#error he abhi


import matplotlib.pyplot as plt
#import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
xdata= np.asarray([1.2,2.6,3.6,9.5,6.11,8.51,12.55,18.52,45.12,65.12])
ydata= np.asarray([8.9,12.56,24.21,32.12,7.56,12.65,35.65,41.1,21.4,44.88])
xdata=xdata.reshape(10,1)
ydata=ydata.reshape(10,1)
print(xdata)
a= np.linspace(0,50,20)
a=a.reshape(20,1)
algo= LinearRegression()
algo.fit(xdata,ydata)
plt.scatter(xdata,ydata,lable="training data")
b= algo.predict(a)
plt.plot(a,b,label="test response")
z=np.asarray([20,2])
z=z.reshape(1,1)
print(algo.predict(z))
plt.legend()
plt.show()
