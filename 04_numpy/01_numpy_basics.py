import numpy as np
print("Numpy version:",np.__version__)
# Create 1D, 2D, and 3D arrays using numpy
# 1D array: A one-dimensional array is a linear list of elements.
arr=np.array([1,2,3])
print("1D Array:",arr)

# 2D array: A two-dimensional array is a matrix with rows and columns.
# It can be visualized as a grid of elements.
arr2d=np.array([[1,2],[3,4]])
print("2D Array:",arr2d)
 
 #3D array: A three-dimensional array can be thought of as a cube of elements.
# It has depth in addition to rows and columns.
arr3d=np.array([[1,2],[3,4],[5,6]])
print("3D Array:",arr3d)

#Array properties
print("shape of 2d array:",arr2d.shape)
print("size of 3d array:",arr3d.size)
print ("data type of 1d array:",arr.dtype)

