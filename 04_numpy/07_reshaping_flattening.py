import numpy as np
print("=== Reshaping and Flattening Arrays ===")
#------------------------------------
print("original array:")
a=np.arange(1,7)
print("a:",a)
print("shape of a:",a.shape)

#---------------------------------
print("reshaping to 2D array:")
reshaped=a.reshape((2,3))
print("reshaped:",reshaped)
print("shape of reshaped:",reshaped.shape)
#---------------------------------
