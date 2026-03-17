import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix=[]

for i in range(rows):
    row = list(map(int, input("Enter the elements of row {}: ".format(i+1)).split()))
    matrix.append(row)


a = np.array(matrix)


print("Original Matrix:" , a)


print(int(np.average(a)))

print(np.argmin(a))



