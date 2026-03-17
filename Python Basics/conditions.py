# question1

age = int(input("Please enter your age: "))

if age < 13:
    print("You are a child.")

elif age < 20:
    print("You are a teenager.")

else:
    print("You are an adult.")


# -----------------
# question2

age = int(input("Please enter your age: "))
day = input("Please enter the day of the week: ")

price = 10

if age >= 18 and day.lower() == "wednesday":
    price -= 2
else:
    price = 8

print("The price of the ticket is:", price)


# -----------------
# question3

marks = int(input("Please enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")

elif marks >= 90 and marks <= 100:
    print("Grade: A")

elif marks >= 80 and marks < 90:
    print("Grade: B")

elif marks >= 70 and marks < 80:
    print("Grade: C")

elif marks >= 60 and marks < 70:
    print("Grade: D")

else:
    print("Grade: F")


# -----------------
# question4

password = input("Please enter your password: ")

if len(password) < 8:
    print("Password is too short. It must be at least 8 characters long.")

elif len(password) >= 8 and len(password) < 12:
    print("Password is acceptable, but consider using a longer password for better security.")

elif len(password) >= 12:
    print("Password is strong.")


# -----------------
# question5

year = int(input("Please enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


# -----------------
# question6

pet = input("Please enter your favorite pet: ")
age = int(input("Please enter your pet's age: "))

food = ""

if pet.lower() == "dog" and age < 2:
    food = "puppy food"

elif pet.lower() == "cat" and age > 5:
    food = "senior cat food"

print("Recommended food:", food)