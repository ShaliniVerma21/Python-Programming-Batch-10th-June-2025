# ===============================
# Greet the user
# ===============================

# input() is used to take input from the user
name = input("Enter your name: ")  
print(f"Welcome, {name}!")  # f-string used to include variable in string

# ==================================
# VARIABLES
# ==================================
# A variable is a named container to store data.
# Python is dynamically typed. No need to declare data types.

# Syntax:
# variable_name = value
name =123
name ="hello"

# Examples:
name = "Shalini"
age = 28
city = "Mumbai"
fees = 5000.75
is_available = True
temperature = 37.5
mobile = "9876543210"
email = "shalini@example.com"
grade = 'A'
distance_km = 12.3

# ==================================
# DATA TYPES
# ==================================
"""
Python supports the following data types:
1. int         - Integer (e.g., 10)
2. float       - Decimal numbers (e.g., 5.67)
3. str         - Text data (e.g., "hello")
4. bool        - Boolean (True/False)
5. list        - Ordered, changeable, allows duplicates
6. tuple       - Ordered, unchangeable, allows duplicates
7. set         - Unordered, no duplicates
8. dict        - Key-value pairs
9. NoneType    - Represents no value
"""

# Real-world examples:
units = 10                 # int
price = 99.99              # float
product = "Laptop"         # str
is_active = True           # bool
items = ["pen", "book"]    # list
dimensions = (20, 15, 10)  # tuple
unique_ids = {101, 102}    # set
student = {"name": "Shalini", "age": 22}  # dict
data = None                # NoneType

# Type checking
print(type(price))  # Output: <class 'float'>

# ==================================
# OPERATORS IN PYTHON
# ==================================
"""
Operators are used to perform operations on variables and values.
Types:
1. Arithmetic
2. Relational (Comparison)
3. Assignment
4. Logical
5. Bitwise
6. Membership
7. Identity
"""

# ==================================
# 1. ARITHMETIC OPERATORS
# +, -, *, /, %, **, //

a = 15
b = 4

print(a + b)  # Addition: 19
print(a - b)  # Subtraction: 11
print(a * b)  # Multiplication: 60
print(a / b)  # Division: 3.75
print(a % b)  # Modulus: 3
print(b ** 2)  # Exponent: 16
print(a // b)  # Floor Division: 3

# Real-life:
price = 50
quantity = 3
print("Total:", price * quantity)

marks = (80 + 70 + 90) / 3
print("Average:", marks)

seconds = 250
print("Minutes:", seconds // 60)

# ==================================
# 2. RELATIONAL OPERATORS
# ==, !=, >, <, >=, <=

age = 20
print(age >= 18)  # True

marks = 45
print(marks >= 40)  # True

amount = 999
print(amount < 1000)  # True

entered_pin = 1234
real_pin = 4321
print(entered_pin == real_pin)  # False

temp = 25
print(temp != 30)  # True

height = 154
print(height > 150)  # True

weight = 65
print(weight <= 70)  # True

name = "Shalini"
print(name == "Shalini")  # True

price = 200
print(price >= 100 and price <= 500)  # True

num = 6
print(num % 2 == 0)  # Even check: True

# ==================================
# 3. ASSIGNMENT OPERATORS
# =, +=, -=, *=, /=, %=, **=, //=

x = 10
x += 5
x -= 3
x *= 2
x /= 4
x %= 4

# Use case:
salary = 10000
salary += 2000  # 12000

steps = 1000
steps += 500

total = 0
item_price = 250
total += item_price

lives = 3
lives -= 1

wallet = 1000
wallet -= 250

# ==================================
# 4. LOGICAL OPERATORS
# and, or, not

age = 20
has_id = True
print(age >= 18 and has_id)  # True

username = "admin"
password = "123"
print(username == "admin" or password == "admin")  # True

is_busy = False
print(not is_busy)  # True

grade = 'A'
attendance = 90
print(grade == 'A' and attendance > 85)  # True

income = 30000
credit_score = 750
print(income > 25000 and credit_score >= 700)  # True

height = 150
age = 12
print(height >= 140 and age >= 10)  # True

total_amount = 400
coupon = True
print(total_amount > 500 or coupon)  # True

msg = ""
print(not msg)  # True if empty string

print(age >= 18 and has_id)  # Driving license

is_weekend = True
is_holiday = False
print(is_weekend or is_holiday)  # Day off?

# ==================================
# 5. BITWISE OPERATORS
# &, |, ^, ~, <<, >>

a = 5  # 0101
b = 3  # 0011

print(a & b)  # AND: 1
print(a | b)  # OR: 7
print(a ^ b)  # XOR: 6
print(~a)     # NOT: -6
print(a << 1)  # Left shift: 10
print(a >> 1)  # Right shift: 2

read = 4
write = 2
execute = 1
user = read | write  # 6 (Read + Write)

x = 7  # 0111
mask = ~1
print(x & mask)  # Turn off last bit: 6

num = 4
print(num & 1 == 0)  # Even check: True

# Swap numbers using XOR
x = 10
y = 20
x = x ^ y
y = x ^ y
x = x ^ y

# ==================================
# 6. MEMBERSHIP OPERATORS
# in, not in

fruits = ["apple", "banana", "mango"]
print("banana" in fruits)     # True
print("grapes" not in fruits)  # True

email = "shalini@example.com"
print("@" in email)  # Valid email check

text = "Python is powerful"
print("Python" in text)  # True

usernames = ["admin", "test"]
print("admin" in usernames)

print("a" in "data")

permissions = "rw"
print("r" in permissions and "w" in permissions)

banned = ["abc", "xyz"]
print("user1" not in banned)

courses = ["Python", "Java"]
print("Python" in courses)

coupon_codes = ["SAVE50", "NEW100"]
print("SAVE50" in coupon_codes)

# ==================================
# 7. IDENTITY OPERATORS
# is, is not

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)        # True (same object)
print(a is not c)    # True (different object)
x = None
print(x is None)     # True

print(id(a) == id(b))  # Same memory

x = 100
y = 100
print(x is y)  # True (Python caches small ints)

a.append(4)
print(b)  # [1, 2, 3, 4]

s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True

print(id(c))  # Different ID than 'a' and 'b'

b = [5, 6]
print(a is b)  # False

print(a == c)  # True (values same)
print(a is c)  # False (objects different)


#-------------------------------------------------------------------------------------------------------------

# Real life examples : 

# 1. Checking if a user is logged in or not

logged_in = True
if logged_in:
    print("Welcome, you are logged in")
else:
    print("Please login to access this feature")


# 2. Checking if a user has a certain permission

has_permission = True
if has_permission:
    print("You have permission to access this feature")
else:
    print("You do not have permission to access this feature")


# 3. Checking if a user has a certain role

has_role = True
if has_role:
    print("You have the role of admin")
else:
    print("You do not have the role of admin")


# 4. Checking if a user has a certain status

has_status = True
if has_status:
    print("You have the status of active")
else:
    print("You do not have the status of active")


# 5.Checking if a user has a certain skill
has_skill = True
if has_skill:
    print("You have the skill of programming")
else:
    print("You do not have the skill of programming")
