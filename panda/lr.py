import numpy as np 
import matplotlib.pyplot as plt 

from sklearn import linear_model
house_floor=np.array([1,2,3,4,5,6])
house_price=np.array([5000,7000,15000,18000,22000,28000])
print(np.mean(house_floor))
house_floor=house_floor.reshape(-1,1)
house_floor.ndim
#lr=linear_model.LinearRegression()
lr=linear_model.LinearRegression(copy_X=True,fit_intercept=True,n_jobs=1,normalize=False)
lr.fit(house_floor,house_price)
PREDICT=[[1],[15]]
p=lr.predict(PREDICT)
#array([4190.47619048,69390.47619048])
plt.plot(PREDICT,p,color='red')
plt.scatter(house_floor,house_price)
plt.scatter(PREDICT,p,color='green',s=250)
plt.show()
