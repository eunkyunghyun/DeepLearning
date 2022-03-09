import numpy as np

# Create a linear array whose type is int32.
a = np.array([1, 2, 3])
print(a, a.dtype)

# Create a linear array whose type is float64.
b = np.array([1.1, 1.2, 3])
print(b, b.dtype)

# Create a quadratic array whose type is default.
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c, c.dtype)

# Create a quadratic array whose type is float64.
d = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
print(d, d.dtype)

# All of the array's elements are filled with numerical zero.
a = np.zeros((3, 4))
print(a, a.dtype)

# All of the array's elements are filled with numerical one.
b = np.ones((2, 2))
print(b, b.dtype)

# All of the array's elements are filled with vacant type's thresholds in the numpy module.
c = np.empty((3, 3))
print(c, c.dtype)

# Create an array that is comprised of a form of an arithmetic sequence.
a = np.arange(1, 10, 1)
print(a)

# Create an array whose length of elements is divided up into what you set.
b = np.linspace(0, 100, 100)
print(b)

# Conserve all the data stored in the array, but alter its dimension.
print(b.reshape(5, 20))
