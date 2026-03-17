# strings are immutable means you cannot change their content after creation. You can create a new string by concatenating or slicing existing strings.

print("rakesh")

"rakesh" * 2

print("rakesh" + "Jain")
name = "suman"

print(name[0])

# strings function

print(name[0:3])

print(len(name))

print(name.upper())

str = "   rakesh   "
print(str.strip())

str1 = "repalceme"
print(str1.replace("me", "you"))

print(str1.find("e"))

print(str1.count("e"))

s = "apple mango banana"
print(s.split())

words = ["Python", "is", "easy"]

print(" ".join(words))

for char in name:
    print(char)







