import math

import numpy as np
t=np.empty([32561,15],dtype=str)
t=np.loadtxt('adult_data.txt',dtype=str,delimiter=',')
wenhao=" ?"
print(t.shape)
uniques=np.unique(t,axis=0)
print(uniques.shape)
result=np.flatnonzero(np.core.defchararray.find(uniques,wenhao)!=-1)
print(result)
sb=np.floor(result/15)
sb=sb.astype(np.int16)
sb=np.unique(sb,axis=0)
print(sb)
uniques=np.delete(uniques,sb,axis=0)
print(uniques.shape)
print(uniques)

np.savetxt('adult_data1.txt',uniques,fmt='%s')

