import math

import numpy as np
# Create a empty matrix to store the row data
raw_data=np.empty([32561,15],dtype=str)
raw_data=np.loadtxt('adult_data.txt',dtype=str,delimiter=',')
print(raw_data.shape)
# Clean the duplicate data
uniques_data=np.unique(raw_data,axis=0)
print(uniques_data.shape)
# Clean the missing data (row which contains " ?")
missing_data_sign=" ?"
row_index=np.flatnonzero(np.core.defchararray.find(uniques_data,missing_data_sign)!=-1)
print(row_index)
row_number=np.floor(row_index/15)
row_number=row_number.astype(np.int16)
row_number=np.unique(row_number,axis=0)
print(row_number)
uniques_data=np.delete(uniques_data,row_number,axis=0)
#Data has been cleaned
print(uniques_data.shape)
print(uniques_data)
#Save data
np.savetxt('adult_data_cleaned.txt',uniques_data,fmt='%s')