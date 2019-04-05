#coding in python
import math
longText = """
This is some
Really
Long text
"""
first = "Simba"
last = "Mupfukudzwa"
full = f"{first} {last}"
song = "Crazy Train"
text = "escape \"from the bronx"
students_count = 1000
rating = 5.34
is_active = True
course_name = ""
x, y = 2, 4
a = b = 45
print(full)
print(type(is_active))
print(type(course_name))
print(type(rating))
print(type(students_count))
print(id(rating))
rating += 10
print(id(rating))
print(len(song))
print((song[0:5]))
print((song[6:]))
print(id(song))
print(text)
print(longText)

print("******************************************")
print("LISTS")
print("******************************************")
some_list = [3, 4]
print(some_list)
print(id(some_list))
some_list.append(100)
print(id(some_list))

print("******************************************")
print("STRINGS")
print("******************************************")
word = " Python Programming power"
print(word.upper())
print(word.capitalize())
print(word.lower())
print(word.title())
print(word.upper().strip())
print(word.find('power'))
print(word.replace('o', '@'))
print("power" in word)  # True
print("power" not in word)  # False
print("******************************************")
print("NUMBERS")
print("******************************************")
x = 10  # number
print(x)
x = 0b10  # binary
y = 0x12c  # hecadecimal
print("0b10 binary is :", x)
print(y)
print(bin(x))  # actually binary representation
print(hex(y))  # actually hexadecimal representation
x = 1 + 2j
print(x)

print("******************************************")
print("ARITHMETIC OPERATIONS")
print("******************************************")
x = 100
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(10 / 3)
print(10 % 3)
print(2**3)
print("******************************************")
print("WORKING WITH NUMBERS PART 2")
print("******************************************")
PI = 3.14
print(PI)
print(PI * 23)
print(round(PI * 23))
print(abs(PI * 100))
print(math.floor(PI))
print("******************************************")
print("CONDITIONAL STATEMENTS")
print("******************************************")
age = 12
if age >= 65:
    print("Get ready to retire")
elif age <= 18:
    print("Too young to work")
else:
    print("Get a job!")
print("End of assessment")

print("******************************************")
print("LOGICAL OPERATORS")
print("******************************************")
# not and or
total = 10
name = "Simba"
if not name:
    print("Empty")
else:
    print("Your name is " + name)

score = "win" if total > 20 else "loose"
print(score)

print("******************************************")
print("PYTHON LOOPS - FOR")
print("******************************************")
# Only 2 types : for and while...
# Strings in python are iterable
data = [2, 5, 7, 9]
for num in data:
    print(num + 100)

for num in range(0, 80, 20):
    print(num)

    # range does not return a list
    # range is an object
    # range takes a very small amount of memory & is iterable
names = ["James", "Allen", "John", "Cindy", "Solomon"]
jnames = []
for name in names:
    if name.startswith("B"):
        print(name)
else:
    print("No match found")

print("******************************************")
print("PYTHON LOOPS - WHILE")
print("******************************************")

# score = 100
# guess = 0

# while score != guess:
#     guess = input("Guess The Score : ")

print("******************************************")
print("PYTHON FUNCTIONS")
print("******************************************")


def inc(num, by):
    return (num, num + by)





print(inc(2, 3))

# Tiple is a read only list
# Create tuple by using parentheses
print(inc(5, by=100))  # keyword argument
