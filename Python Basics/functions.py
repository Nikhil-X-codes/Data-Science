# question1
def square(num):
    return num ** 2

ans=square(5)
print(ans)



# question2
def circle(radius):
    area=3.14*radius**2
    circum=2*3.14*radius
    return area,circum

area,circum=circle(5)
print("Area:",area) 
print("Circumference:",circum)




# question3
def greet(name = "World"):
    return f"Hello, {name}!"

print(greet())
print(greet("Alice"))





# question4            (lamba A lambda function is a one-line function without a name used for small operations.)

# syntax : lambda arguments: expression

cube = lambda x: x ** 3
print(cube(3))






# question5                 (*args is used in a function when we do not know how many arguments will be passed to the function.it stored in a tuple)
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3,4))







#question6                 (**kwargs is used in a function when we want to pass a variable number of keyword arguments to the function.it stored in a dictionary)
def print_info(**kwargs):
    for key, value in kwargs.items():
     print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")






#question7   

def factorical(n):
   if n == 0 or n == 1:
      return 1

   return n * factorical(n - 1)

print(factorical(5))    



# Higher order functions(is a function that takes another function as an argument or returns a function as a result.)

def apply_operation(a, b):
   def func(x, y):
      return x + y
   
   return func(a, b)

print(apply_operation(2,4))


