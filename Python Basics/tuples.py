# tuples are immutable (cannot be changed after creation)


# packing (creating a tuple)
student = ("Nikhil", 21, "CSE")

for item in student:
    print(item)


# unpacking (assigning values from a tuple to variables)
name, age, branch = student
print(name)  
print(age)   
print(branch)  


# converting tuple to list
data = list(student)
print(data)


# converting tuples to dictionary
t = (("a",1),("b",2),("c",3))
d = dict(t)
print(d)


