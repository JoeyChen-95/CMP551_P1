import math

import numpy as np
t=np.empty([32561,15],dtype=str)
t=np.loadtxt('adult_data.txt',dtype=str,delimiter=',')
print(t)
# print(train_data[32560,14])
wenhao=" ?"
result=np.flatnonzero(np.core.defchararray.find(t,wenhao)!=-1)
print(result)

sb=np.ceil(result/15)
print(sb)