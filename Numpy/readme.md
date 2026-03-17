# NumPy Basics

## 1. What is NumPy?

NumPy (Numerical Python) is a Python library used for working with numbers, arrays, and mathematical operations efficiently.

It provides a powerful data structure called **ndarray (N-dimensional array)** which helps perform numerical computations faster than normal Python lists.

---

## 2. Why Use NumPy?

- It supports **large and multi-dimensional arrays and matrices**.
- It provides many **mathematical functions** to work with numerical data.
- It performs calculations **much faster than Python lists**.

---

## 3. Features of NumPy

### 1. Efficient Array Operations
NumPy provides optimized functions for array operations.  
These operations are **faster than traditional Python lists**.

### 2. Vectorization
Vectorization allows operations on **entire arrays at once without using loops**, which makes the code faster.

### 3. Broadcasting
Broadcasting allows **operations between arrays of different shapes and sizes** automatically.

### 4. C-Speed Under the Hood
NumPy is implemented using **C and Fortran**, which makes numerical computations **very fast**.

### 5. Rich API
NumPy provides many built-in functions for:

- Mathematical operations  
- Linear algebra  
- Random number generation  
- Statistical calculations  

This makes it very useful for **data analysis and scientific computing**.

---

## 4. Limitations of NumPy

### 1. Fixed Data Type
NumPy arrays usually store **elements of the same data type**.  
Unlike Python lists, it is difficult to mix different data types.

### 2. High Memory Usage for Small Tasks
For very small datasets, NumPy may use **more memory than normal Python lists**.

### 3. Learning Curve
Beginners may find NumPy **a little difficult at first** because of array shapes and operations.

### 4. Not Ideal for Non-Numerical Data
NumPy is mainly designed for **numerical computations**, so it is not suitable for text or mixed data.

---

## Conclusion
NumPy is a powerful Python library used for **fast numerical computation, array operations, and scientific computing**. It improves performance and simplifies mathematical operations in Python.