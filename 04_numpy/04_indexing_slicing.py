import numpy as np

print("=== 1️⃣ Basic Indexing on 1D Array ===")
a=np.array([10,20,30,40,50])
print("Original array:",a)
print("First element:",a[0])
print("Last element:",a[-1])
# ------------------------------------------------------------------------
print("\n=== 2️⃣ Slicing on 1D Array ===")
print("a[1:4]:",a[1:4])
print("a[:4]:",a[:3])
print("a[::2]:",a[::2])
print("reversed a[::-1]:",a[::-1])
# ------------------------------------------------------------------------
print("\n=== 3️⃣ Indexing on 2D Array ===")
b=np.array([[1,2,3],[4,5,6]])
print("Original 2D array:\n",b)
print("Element at (0,0):",b[0,0]) #1
print("Element at (1,1):",b[1,1])
# ------------------------------------------------------------------------
print("\n=== 4️⃣ Slicing on 2D Array ===")
print("First Row:",b[0,:])  # First row
print("Second column:",b[:,2]) #Second row
print("Subarray(top-left 2 *2\n)",b[0:2,0:2])
# ------------------------------------------------------------------------
print("\n=== 5️⃣ Fancy Indexing ===")
c=np.array([[5,10,15],[20,25,30]])

#select specific rows or columns
rows=np.array([0,1])
print("Row 0 and 2:\n",c[rows,:]) #output must be: [5,10,15],[20,25,30]
cols=np.array([0,2])
print("Column 0 and 2:\n",c[:,cols]) # output must br: [5,15],[20,30]
#Select specific elements
print("Elements at (0,0) and (1,2):",c[[0,1],[0,0]])
# ------------------------------------------------------------------------
print("\n=== 6️⃣ Boolean Indexing ===")
mask=b>3
print("Mask for elements >3:\n",mask)
# ------------------------------------------------------------------------
print("\n=== 7️⃣ Conditional Replacement ===")
#Replace elements > 5 with 0
d=c.copy()
d[d > 15]=0
print("Array after replacing elements > 5 with 0:\n",d)
#---------------------------------------------------------------------------
print("\n=== 8️⃣ Advance:Step Slicing on 2D Array===")
#every second row and column
print("Every second row and column:\n",c[::2,::2]) # output must be: [5 15]