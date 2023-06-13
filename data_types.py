# Data types

# Numbers -> float, int, complex,
# Strings -> text
# Booleans -> True or False


# Arithmetic operators

# +, -, /, *, %

# Comparison operators

# >, <, ==, !=, >=, <=

# Numeric Types

a = 24
b = 16

# print(a+b)
# print(a-b)
# print(a/b)
#
# print(a<b)

FloatNum = 1.356
IntNum = 4

# print(type(FloatNum + IntNum))

one_third = 1 / 3

# print(one_third)
# print(one_third*3)

# Strings

# single_quotes = 'single quotes'
# doubles_quotes = "double quotes"
#
# print(type(single_quotes))
# print(type(doubles_quotes))
#
# string_failure = "i said 'wow'"
# print(string_failure)
#
# escape_example = 'I said \'Wow\''
#
# print(escape_example)

# String Slicing

hi="Hello World"
#
# print(hi[-11])

# String Methods

# # len()
# print(len(hi))
#
# # strip()
# white_space = "lots of white space                          "
# print(len(white_space))
# print(len(white_space.strip()))
#
# # .lower()
# # .upper()
#
# # .count
#
# fruits = ['apple', 'banana', 'cherry']
#
# x = fruits.count("cherry")
#
# print(x)
#
# # .replace
#
# print(white_space.replace("space", "Space (replaced)"))
#
# # Concatenation & casting

x = 2
y = 5.4
z= "This is a string"
zz = "This is also a string"


print(z + " " + zz)
print(str(x)+" "+z + " " + zz)

# String to numeric casting

int_string = "6"

print(int(int_string))

# F-Strings

name = "lassie"
year = 7
height_cm = 60.2

print(f"{name.upper()} is my dog. he is {year * 7} years old in human years and {height_cm}cm tall")

pi = 3.14159265359

print(f"pi to e decimal places: {pi:.3f}")

# percentages

score = 16
max_score = 26

print(f"You scored {score / max_score}")
print(f"You scored {score / max_score:.0%}")

