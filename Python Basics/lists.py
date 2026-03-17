data = [10, "python", 3.5]

# read operations
for item in data:
    print(item)

print(data[1:2])



#create operations
data.append("new item")

print(data)

data.insert(1, "inserted item")

print(data)

data.extend([1, 2, 3])

print(data)



# update operations
data[0] = 20

print(data)



# delete operations
data.remove("python")

print(data)

data.pop(2)                            

print(data)

del data[1]

print(data)


# list functions
print(len(data))

print(max([1, 5, 3, 9]))

print(sum([1, 2, 3, 4]))

num = [30,9,10,5]
num.sort(reverse=True)

print(num)

num.reverse()

print(num)


# converting list to tuple
my_tuple = tuple(data)
print(my_tuple)


# converting list to dictionary
lst = [("a", 1), ("b", 2), ("c", 3)]
d = dict(lst)
print(d)

# zip function (combining multiples iterables into a single iterable)


list1 = [1, 2, 3]
tuple1 = ("a", "b")


zipped = list(zip(list1, tuple1))

print(list(zipped))
print(dict(zipped))  
print(tuple(zipped))


