import numpy as np
import time

N = 1000000

list1 = list(range(N))
list2 = list(range(N))

start_time = time.time()

list_res = 1

for i in range(N):
    list_res = list1[i] * list2[i]

end_time = time.time()

print("Time taken for list multiplication: ", round(end_time - start_time,4), "seconds")

array1 = np.array(list1)
array2 = np.array(list2)

start_time = time.time()
array_res = array1 * array2
end_time = time.time()

print("Time taken for array multiplication: ", round(end_time - start_time,4), "seconds")
