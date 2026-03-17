student = {
    "name": "Nikhil",
    "age": 21,
    "branch": "CSE"
}

# read operation
for key in student:
    print(key , ":", student[key])


# create operation
student["college"] = "IIIT Sonepat"


# update operation
student["age"] = 22



# delete operation
del student["branch"]

print(student)

student.clear() 

print(student)



# Dictionary Functions

student = {"name":"Nikhil","age":21}

print(student.keys()) 

print(student.items())

print(len(student))

for key,value in student.items():
    print(key,value)

print(student.get("name"))


# converting dictionary to list
data = list(student.items())

# converting dictionary to tuple
d = {"a":1,"b":2}
t = tuple(d.items())
print(t)

