#ex1
import numpy as np
x = np.arange(21)
print("Original vector:")
print(x)
print("After changing the sign of the numbers in the range from 9 to 15:")
x[(x >= 9) & (x <= 15)] *= -1
print(x)

#ex2
import numpy as np
v = np.arange(15,55)
print("Original vector:")
print(v)
print("All values except the first and last of the said vector:")
print(v[1:-1])

#3
import numpy as np
a = np.arange(10,22).reshape((3, 4))
print("Original array:")
print(a)
print("Each element of the array is:")
for x in np.nditer(a):
  print(x,end=" ")
  
#4
import numpy as np
a = np.arange(10,22).reshape((3, 4))
print("Original array:")
print(a)
print("Each element of the array is:")
for x in np.nditer(a):
  print(x,end=" ")
  
#5
import numpy as np
x = np.random.randint(0, 11, 5)
print("Vector of length 5 filled with arbitrary integers from 0 to 10:")
print(x)

#6
import numpy as np
x = np.array([1, 8, 3, 5])
print("Vector-1")
print(x)
y= np.random.randint(0, 11, 4)
print("Vector-2")
print(y)
result = x * y
print("Multiply the values of two said vectors:")
print(result)

#7
import numpy as np
m= np.arange(10,22).reshape((3, 4))
print(m)

#8
import numpy as np
m= np.arange(10,22).reshape((3, 4))
print("Original matrix:")
print(m)
print("Number of rows and columns of the said matrix:")
print(m.shape)

#9
import numpy as np
x = np.zeros((4, 4))
x[::2, 1::2] = 1
x[1::2, ::2] = 1
print(x)

#10
import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",array1)
array2 = [10, 30, 40]
print("Array2: ",array2)
print("Common values between two arrays:")
print(np.intersect1d(array1, array2))

#11
import numpy as np
x = np.array([10, 10, 20, 20, 30, 30])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))
x = np.array([[1, 1], [2, 3]])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))

#12
import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result1 = np.cross(p, q)
result2 = np.cross(q, p)
print("cross product of the said two vectors(p, q):")
print(result1)
print("cross product of the said two vectors(q, p):")
print(result2)

#13
import numpy as np
z= np.random.random((10,2))
x,y = z[:,0], z[:,1]
r = np.sqrt(x**2+y**2)
t = np.arctan2(y,x)
print(r)
print(t)

#14
import numpy as np
x = np.arange(100)
print("Original array:")
print(x)
a = np.random.uniform(0,100)
print("Value to compare:")
print(a)
index = (np.abs(x-a)).argmin()
print(x[index])
