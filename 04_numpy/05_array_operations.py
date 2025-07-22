import numpy as np

a=np.array([1,2,3])
b=np.array([4,5,6])

print("a:", a)
print("b:", b)

print("\n=== 1️⃣ Basic Array Element-wise Operations ===")
print("Addition (a+b):",a+b)
print("Subtraction (a-b):",a-b)
print("Multiplication (a*b):",a*b)
print("Division (a/b):",a/b)
print("Power (a**2):",a**2)


print("\n=== 2️⃣ Universal Functions(ufuncs) ===")
print("Sin of a",np.sin(a))
print("Square root (np.sqrt(b)):",np.sqrt(b))
print("Exponential (np.exp(a)):",np.exp(a))


print("\n=== 3️⃣ Aggregation Functions ===")
print("Sum of a:",np.sum(a))
print("Mean of b:",np.mean(b))
print("Max of b:",np.max(b))
