import numpy as np
x = np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])

#We could reshape it by doing either:

y = x.reshape((3,4))
print(y)
print(y[0,2])
print(x.dtype)
print(x.size)
z= x.reshape(0)
print(z)
#x.shape = (2, 5)
