# Intro to Python

Python is a dynamically typed language, so you do not have to specific the data type of the variables you use. It gets assigned at runtime.

a variable is a named storage location that holds a value. It allows you to store and manipulate data within your code. In this example "message" would be the variable name.
``` python

message = "Hello, World!"

print(message)

```
You can assign data to a variable by using the equals sign symbol.
``` python
# Dynamically typed language - Python

a = 1
b = 2
c = 3.5
hi = "hello world!"
```
## Data Types
The code listed above mentions three main data types: numbers, strings, and booleans.

With numbers, you can have int and float. A float is named this way since the decimal point can float within the numbers.

## Arithmetic Operators

Python supports various arithmetic operators:

    Addition: +
    Subtraction: -
    Division: /
    Multiplication: *
    Modulus: %
## Comparison Operators

Python provides comparison operators to compare values:

    Greater than: >
    Less than: <
    Equal to: ==
    Not equal to: !=
    Greater than or equal to: >=
    Less than or equal to: <=

## Strings

Strings can be defined using single or double quotes:

``` python

hi = "Hello World"
```

## String Slicing

You can access specific characters in a string using slicing:

```python

print(hi[0:5])

# returns "Hello" 

```

## String Methods

Python provides several built-in methods for string manipulation:

    len(): Returns the length of a string
    strip(): Removes leading and trailing whitespace from a string
    lower(): Converts a string to lowercase
    upper(): Converts a string to uppercase
    count(): Counts the occurrences of a substring in a string
    replace(): Replaces a substring with another substring

## Concatenation & Casting

Strings can be concatenated using the + operator, and other data types can be cast to strings:

```python

x = 2
y = 5.4
z = "This is a string"
zz = "This is also a string"

print(z + " " + zz)
print(str(x) + " " + z + " " + zz)
```
## String to Numeric Casting

You can convert a string to an integer using the int() function:

```python

int_string = "6"
print(int(int_string))
```

## F-Strings

F-Strings allow for dynamic string formatting using variables and expressions:

``` python

name = "lassie"
year = 7
height_cm = 60.2

print(f"{name.upper()} is my dog. He is {year * 7} years old in human years and {height_cm}cm tall")
```
## Percentages

Python can calculate and format scores as percentages:

```python

score = 16
max_score = 26

print(f"You scored {score / max_score}")
print(f"You scored {score / max_score:.0%}")
```
## Booleans

In Python, booleans represent two possible values: True and False. Booleans are often used in logical operations and conditional statements to determine the flow of a program.

```python

a = True
b = False
```
## Using Keywords

Python provides keywords for boolean operations:

    Logical AND (and): Returns True if both operands are True.
    Logical OR (or): Returns True if at least one of the operands is True.
    Logical NOT (not): Returns the opposite boolean value of the operand.

```python

 print(True and False) # False
 print(True or False) # True
 print(False or False) # False
```


## Boolean Methods

Python provides boolean methods that can be used to check certain conditions on strings. Some examples include:

    isalpha(): Returns True if all characters in a string are alphabetic (no whitespace or punctuation).
    islower(): Returns True if all characters in a string are lowercase.
    endswith(): Returns True if a string ends with a specified suffix.
    startswith(): Returns True if a string starts with a specified prefix.

```python
hi = "Hello world!"

print(hi.isalpha()) # False
print(hi.islower()) # False
print((hi.endswith("d"))) # False
print(hi.startswith("H")) # True
```
## The Value of 0

The integer value 0 has a boolean representation. In Python, any non-zero value is considered True, while 0 is considered False.

```python

x = 0
y = 10

print(bool(x))
print(bool(y))
```
## None

In Python, None is a special object that represents the absence of a value. It is commonly used to indicate a missing or undefined value.

```python

x = None

print(None == None)
print(x == False)
print(x == True)
print(x is None)
```
In the above code, we compare the value of x with None and False using the equality operator (==) and the identity operator (is).

## Get User Details
To get the user input, you can use the input() function to prompt the user for input. Here's an example:

```python

name = input("What is your name?\n")
age = int(input("What is your age?\n"))
dob = input("What is your date of birth?\n")
address = input("What is your address?\n")
```
In the above code, we use the input() function to ask the user for their name, age, date of birth, and address. The user's responses are stored in the corresponding variable names.

To display the user's details, you can use a F string.
``` python
print(f"Your name is {name}, your age is {age}, your date of birth is {dob}, your address is {address}")
```