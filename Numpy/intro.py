import numpy as np
print(np.__version__)

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1,2],[3,4]])

print(type(a))

print(b.shape)




# update and delete operations
a[1] = 10

e = np.delete(b,1,axis=0)

f = np.delete(b,1)



# read operations

for element in np.nditer(e):
    print(element)

# IMPORTANT NUMPY FUNCTIONS FOR DATA SCIENCE

print(np.sum(a))
print(np.std(a))
# and many more functions are available in NumPy for various mathematical and statistical operations.




# Aggregation Functions

print(np.max(b))
print(np.argmin(a))

# many more aggregation functions are available in NumPy, such as mean, median, variance, etc., which are commonly used in data analysis and scientific computing.



# randomly geenrates 5 nos from range
print(np.random.randint(1,10,5))  



# randomly generated nos from standard normal distribution
print(np.random.randn(3,3))



# Linear Algebra Functions


m1 = np.array([[1,2],
              [3,4]])

m2 = np.array([[5,6],
              [7,8]])

print(np.dot(m1,m2))


# inverse of matrix only exists for square matrices that are non-singular (i.e., they have a non-zero determinant).
print(np.linalg.inv(m1))


# determinant of a square matrix 
print(np.linalg.det(m1))



