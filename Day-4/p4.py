# 1. Print Message (Output)

# Printing simple messages to the screen
print("Welcome to Python Programming!")  # Greeting message
print("Your total bill is ₹499.")  # Invoice amount
print("Login successful.")  # Login confirmation
print("Thank you for shopping with us.")  # Thanks note
print("Result: Pass")  # Exam result
print("Payment Successful.")  # Payment status
print("Error: Invalid Input")  # Error message
print("Your order has been shipped.")  # Order status
print("Temperature is 38.5°C")  # Showing temperature
print("Good Morning, User!")  # Time-based greeting

# More real-time prints
print("File uploaded successfully.")
print("Battery low. Please charge.")
print("Session expired.")
print("Appointment confirmed.")
print("Ticket booked.")
print("Processing your request...")
print("OTP sent successfully.")
print("Backup completed.")
print("Update available.")
print("Welcome back, Shalini!")


# 2. Input & Output

# Taking input and displaying output
name = input("Enter your name: ")
print("Hello", name)

age = input("Enter your age: ")
print("You are", age, "years old")

city = input("Where do you live? ")
print("You live in", city)

product = input("Enter product name: ")
print("Product selected:", product)

email = input("Enter your email: ")
print("Thanks for registering with:", email)

course = input("Which course are you learning? ")
print("Great choice:", course)

country = input("Which country are you from? ")
print("Greetings from", country)

feedback = input("Your feedback: ")
print("Feedback saved:", feedback)

mobile = input("Enter your mobile number: ")
print("Verification code sent to", mobile)

pin = input("Enter 4-digit PIN: ")
print("PIN accepted")

# Additional real-time input-output examples
username = input("Enter username: ")
print("Welcome,", username)

password = input("Enter password: ")
print("Password saved successfully")

address = input("Enter your address: ")
print("Your address:", address)

hobby = input("Your hobby: ")
print("Wow! You love", hobby)

brand = input("Favorite brand? ")
print("You like", brand)

pet = input("Enter your pet name: ")
print("Hello from", pet)

school = input("Which school did you go to? ")
print("Alumni of", school)

movie = input("Last movie watched? ")
print("Hope you enjoyed", movie)

food = input("Favorite food: ")
print("Yum! I like", food, "too")

color = input("Favorite color: ")
print("Nice choice:", color)


# 3. Comments & Statements

# Comments help explain the code and are ignored during execution

# This is a single-line comment
print("Hello")  # This prints Hello

# Adding two numbers
a = 5
b = 10
print(a + b)  # Output: 15

# Subtracting values
x = 100
y = 20
print(x - y)  # Result: 80

# Display full name
first = "Shalini"
last = "Verma"
print(first + " " + last)  # Combining strings

# Area of circle
radius = 7
pi = 3.14
area = pi * radius * radius  # Formula: πr^2
print("Area is:", area)

# Square of number
num = 6
print("Square:", num ** 2)  # Using exponent

# Welcome message
user = "Student"
print("Welcome,", user)

# Additional real-time commented statements
# Multiplying values
quantity = 3
price = 100
print("Total cost:", quantity * price)

# Checking eligibility
age = 21
print("Eligible for driving:", age >= 18)

# Greeting
name = "Rahul"
print("Hi,", name)

# BMI calculation
weight = 65
height = 1.7
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)

# Celsius to Fahrenheit
c = 25
f = (c * 9/5) + 32
print("Temperature in F:", f)

# Age after 10 years
current_age = 25
print("Age in 10 years:", current_age + 10)

# Print file type
filename = "data.csv"
print("File type:", filename.split('.')[-1])

# Sum of list
numbers = [2, 4, 6]
print("Sum:", sum(numbers))

# Print length of name
name = "Shalini"
print("Length of name:", len(name))

# Convert string to uppercase
text = "python"
print("Uppercase:", text.upper())


#4. Variables

name = "Shalini"
age = 27
city = "Mumbai"
height = 154.5
is_active = True
language = "Python"
salary = 25000
grade = 'A'
course = "Data Analytics"
is_vegetarian = False



# 5. Data Types

# Integer
units = 10

# Float
price = 199.99

# String
name = "Shalini"

# Boolean
is_available = True

# List
fruits = ["apple", "banana", "grape"]

# Tuple
dimensions = (10, 20, 30)

# Set
unique_ids = {101, 102, 103}

# Dictionary
student = {"name": "Shalini", "age": 22}

# NoneType
value = None

# Complex
z = 2 + 3j



# 6. Arithmetic Operators

a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.33
print(a % b)  # Modulus: 1
print(a ** b)  # Exponent: 1000
print(a // b)  # Floor division: 3

# Real examples:
total_price = 299.99 * 3
print("Total:", total_price)

average = (80 + 75 + 90) / 3
print("Average:", average)

seconds = 125
minutes = seconds // 60
print("Minutes:", minutes)


#  7. Relational Operators

print(10 > 5)     # True
print(7 < 2)      # False
print(8 == 8)     # True
print(9 != 6)     # True
print(10 >= 10)   # True
print(4 <= 3)     # False

# Real-world examples
age = 18
print(age >= 18)  # Eligible for vote

marks = 40
print(marks >= 35)  # Pass

discount = 20
print(discount < 50)

height = 160
print(height > 150)

price = 1000
print(price <= 1000)



# 8. Assignment Operators

x = 10
x += 5  # x = x + 5 => 15
x -= 3  # x = x - 3 => 12
x *= 2  # x = x * 2 => 24
x /= 4  # x = x / 4 => 6.0
x %= 5  # x = x % 5 => 1.0
x **= 2  # x = x^2 => 1.0
x //= 2  # x = x // 2 => 0.0

# Real examples
wallet = 500
wallet -= 100  # Payment done
wallet += 50   # Cashback added

score = 0
score += 10


# 9. Logical Operators

age = 20
has_id = True
print(age >= 18 and has_id)  # True

username = "admin"
password = "1234"
print(username == "admin" or password == "admin")  # True

is_busy = False
print(not is_busy)  # True

attendance = 90
marks = 85
print(attendance > 80 and marks > 70)  # True

income = 35000
credit_score = 720
print(income > 25000 and credit_score >= 700)

holiday = False
weekend = True
print(holiday or weekend)  # True



#10. Bitwise Operators

a = 5  # 0101
b = 3  # 0011

print(a & b)   # 0001 => 1
print(a | b)   # 0111 => 7
print(a ^ b)   # 0110 => 6
print(~a)      # -6
print(a << 1)  # 1010 => 10
print(a >> 1)  # 0010 => 2

# Turn off last bit
x = 7  # 0111
print(x & ~1)  # 0110 => 6

# Check if number is even
num = 8
print(num & 1 == 0)  # True


# 11. Membership Operators
fruits = ["apple", "banana", "grape"]
print("apple" in fruits)       # True
print("orange" not in fruits)  # True

text = "Python is fun"
print("Python" in text)        # True

email = "user@example.com"
print("@" in email)            # True

usernames = ["admin", "guest"]
print("test" not in usernames) # True

# Real use cases
coupon = "SAVE50"
valid_coupons = ["SAVE50", "OFF100"]
print(coupon in valid_coupons)


# 12. Identity Operators

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True
print(x is not z)  # True
print(x == z)      # True (values)

a = None
print(a is None)   # True

s1 = "hello"
s2 = "hello"
print(s1 is s2)    # True

age = 30
print(type(age) is int)  # True

p = 100
q = 100
print(p is q)  # True (cached in Python small int)
