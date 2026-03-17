import time

#question1

n = int(input("Enter a number: "))

my_list = []

for i in range(n):
    user_input = int(input("Enter a number: "))
    my_list.append(user_input)

count = 0

for num in my_list:
    if num > 0:
        count+=1

print("The number of positive numbers is: ", count)



#---------------------------------------------------
#question2

n = int(input("Enter a number: "))
my_list = []

sum = 0

for i in range(n):
    user_input = int(input("Enter a number: "))
    my_list.append(user_input)

for num in my_list:
    if num % 2 == 0:
        sum+=num

print("The sum of even numbers is: ", sum)




# -------------------------------------------
#question3

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)


# -------------------------------------------
#question4

str = input("Enter a string: ")
chars = list(str)

i , j = 0 , len(chars) - 1

while i < j:
    chars[i], chars[j] = chars[j], chars[i]
    i+=1
    j-=1

print("Reversed string: ", "".join(chars))


# -------------------------------------------
#question5

s = input("Enter a string: ")

for char in s:
    if s.count(char) == 1:
        print("The first non-repeating character is: ", char)
        break



# -------------------------------------------
#question6

n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n+1):
    factorial *= i

print("The factorial of", n, "is: ", factorial)




# -------------------------------------------
#question7

n = int(input("Enter a number: "))

while n > 10:
    n = int(input("Enter a number: "))

print("You entered a number less than or equal to 10: ", n)





# -------------------------------------------
#question8

n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print(n, "is not a prime number.")
        break
else:
    print(n, "is a prime number.")




# -------------------------------------------
#question9

n = int(input("Enter a number: "))

my_list = []
unique_numbers = set()

for i in range(n):
    user_input = int(input("Enter a number: "))
    my_list.append(user_input)

for num in my_list:
    if num in unique_numbers:
        print("The duplicate number is: ", num)
    else:
        unique_numbers.add(num)




# -------------------------------------------
#question10

max_attempts,retry,timer = 5,0,1

while retry < max_attempts:
    print("Attempt", retry + 1,"and timer is", timer, "seconds")
    time.sleep(timer)
    retry += 1
    timer *= 2


