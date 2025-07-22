import numpy as np

print("=== 1️⃣ Broadcasting Basics ===")

# Adding a scalar to an array
a=np.array([1,2,3])
print("Array a:", a)

scalar=10
result=a + scalar
print("Result of a + scalar:", result)
# NumPy 'stretches' the scalar to match the shape of the array as 10 to [10,10,10]


#----------------------------------------------------------------
print("\n === 2️⃣ Broadcasting with 1D Array to each row of a 2D array ===")

b=np.array([[10,20,30],[40,50,60]])
print("2D Array b:\n", b)

row=np.array([1,2,3])
print("1D Array row:", row)

result=b + row
print("Result of b + row:\n", result)
 

#----------------------------------------------------------------
print("\n=== 3️⃣ Broadcasting with 2D Array to each column of a 2D array ===")

col=np.array([[100],[200]])
print("Column Array col:\n", col)

result=b+ col
print("Result of b + col:\n", result)
# col is broadcasted to match the shape of b, adding each column of col to each column of b

#----------------------------------------------------------------
print("\n=== 4️⃣ Broadcasting with different shapes ===")
c=np.array([[1],[2],[3]]) #shape(3,1)
d=np.array([10,20,30])    #shape(3,)

print("Array c:\n", c)
print("Array d:", d)

result=c * d
print("Result of c * d:\n", result)

