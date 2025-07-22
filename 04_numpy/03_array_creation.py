import numpy as np
# Create an array of zeros  
zeros_array = np.zeros((2, 3))  # 2 rows, 3 columns
ones_array = np.ones((2, 3))    
arange_array=np.arange(0,20,2)  # (from,to,)
linspace_array=np.linspace(0,1,5)
random_arr=np.random.rand(2,3)  # 2 rows, 3 columns with random values
print("Array of zeros:\n", zeros_array)
print("Array of ones:\n", ones_array)
print("Array with arange:\n", arange_array)
print("Array with linspace:\n", linspace_array)
print("Random array:\n", random_arr)