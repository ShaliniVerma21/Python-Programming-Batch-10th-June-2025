"""
1. What is Python Programming?

Python is a high-level, interpreted, general-purpose programming language. 
It was designed to be easy to read and write, making it ideal for beginners and 
professionals alike.
Python is popular in web development, data science, automation, AI/ML, game development, 
and much more.

Real-Life Examples:
1. Instagram and YouTube use Python for backend.
2. Python scripts are used to automate Excel reports.
3. You can create chatbots, calculators, games, and apps.

"""

# 1. Using print() Function
print("Hello, World!") 

# 2. Print with Multiple Arguments
name = "Shalini"
age = 27
print("Name:", name, "Age:", age)

# 3. Using String Concatenation (+)
first = "Hello"
second = "World"
print(first + " " + second)

"""
2. History of Python

Python was developed by Guido van Rossum in the late 1980s and released in 1991.
It was named after the British comedy group "Monty Python".
Python’s philosophy emphasizes code readability, using indentation rather than curly braces.

Versions: Python 2 (legacy), Python 3 (current)

3. Why Learn Python?

Benefits:
1. Simple and easy to learn
2. High demand in the job market
3. Vast libraries and community support
4. Great for both small scripts and large applications

Use Cases:
1. Web development (Django, Flask)
2. Data Analysis (Pandas, NumPy)
3. Machine Learning (Scikit-learn, TensorFlow)
4. Automation (Scripts, Bots)

4. Variables

A variable is a name that stores a value. In Python, you don’t need to declare the type.

Rules:
1. Must start with a letter or underscore
2. Can’t start with a number
3. Can include letters, digits, underscores

"""

name = "Shalini"
age = 28
height = 154.5

print("Name:", name)
print("Age:", age)
print("Height:", height)

"""
5. Keywords

Keywords are reserved words that have a special meaning in Python. 
They cannot be used as variable names.

Examples:
False, True, None, if, else, elif, while, 
for, break, continue, def, return, import, 
as, class, try, except

"""

# Using some keywords in a program
if True:
    print("This is True")

"""
6. Statements & Comments

Statements-->
Instructions that Python can execute.

Comments-->
Used to explain the code. They are ignored by the Python interpreter.

Single-line: starts with #

Multi-line: enclosed in ''' or """


# This is a single-line comment

name = "Shalini"  # storing name
print(name)

"""
7. Python Character Set

Character set refers to all the valid characters Python understands, including:

1. Letters – A to Z, a to z
2. Digits – 0 to 9
3. Special Symbols – + - * / = () {} [] etc.
4. Whitespace – space, tab, newline
5. Other Characters – Unicode characters
"""
# Using letters, digits, special characters
a = 10        # digit
b = 20
sum = a + b   # using + operator
print("Sum:", sum)

# using whitespace for indentation
if a < b:
    print("a is smaller than b")  # whitespace used before print


#-------------------------------------------------------------------------------

#Example 1: Simple Input
name = input("Enter your name: ")
print("Hello,", name)


# Example 2: Input Two Numbers and Add Them
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert to integers
num1 = int(num1)
num2 = int(num2)

print("Sum =", num1 + num2)


#Example 3: Input and Multiply Two Decimal Numbers
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Product =", x * y)


#Example 4: Input Age and Print Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible yet.")


#Program 1: Calculate Area of a Rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle =", area)


#Program 2: Calculate total marks of a students. Subjects : Hindi,English, Maths, History,Arts
marks_hindi = float(input("Enter marks in Hindi: "))
marks_english = float(input("Enter marks in English: "))
marks_math = float(input("Enter marks in Maths: "))
marks_history = float(input("Enter marks in History: "))
marks_arts = float(input("Enter marks in Arts: "))
marks_total = marks_hindi + marks_english + marks_math + marks_history + marks_arts
print("Total marks =", marks_total)


"""
Remember to use int() or float() when you're working with numbers.
The input() function always returns a string, so you need to convert it to a number if
you want to perform mathematical operations on it.
"""

# Without conversion
a = input("Enter number: ")  # string
b = input("Enter another: ")  # string
print(a + b)  # concatenates

# With conversion
a = int(input("Enter number: "))  # integer
b = int(input("Enter another: "))
print(a + b)  # adds
