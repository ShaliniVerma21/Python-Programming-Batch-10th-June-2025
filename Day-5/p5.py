# 1. Print Message – print() Function

# 1. Greet user
print("Welcome to Python Programming!")

# 2. Show today's date
print("Today's date is: 22nd June 2025")

# 3. Show restaurant name
print("You are at 'Shalini's Café'.")

# 4. Thank you message
print("Thank you for shopping with us!")

# 5. Display math result
print("Total = ", 50 + 25)

# 6. Show motivational quote
print("Believe in yourself and all that you are.")

# 7. Display address
print("Address: 101, MG Road, Mumbai - 400001")

# 8. Inform about class timing
print("Python class starts at 10:00 AM")

# 9. Show version info
print("Running Python version 3.11.5")

# 10. End of program message
print("Program execution completed successfully.")


# 2. Variables – Declaring and using variables

# 1. Store name
name = "Shalini"
print("Hello", name)

# 2. Store age
age = 28
print("Age:", age)

# 3. Store temperature
temperature = 37.5
print("Body Temperature:", temperature)

# 4. Store boolean value
is_logged_in = True
print("User logged in:", is_logged_in)

# 5. Store shopping total
total_bill = 350.75
print("Total Bill:", total_bill)

# 6. Store city name
city = "Mumbai"
print("City:", city)

# 7. Store number of students
students = 45
print("Total students:", students)

# 8. Store feedback
feedback = "Excellent service!"
print("Customer Feedback:", feedback)

# 9. Store rating
rating = 4.7
print("App Rating:", rating)

# 10. Store status
is_active = False
print("Account Active:", is_active)


# 3. Data Types – Different Python data types

# 1. String
title = "Python Developer"
print(type(title))

# 2. Integer
year = 2025
print(type(year))

# 3. Float
pi = 3.14159
print(type(pi))

# 4. Boolean
is_online = True
print(type(is_online))

# 5. List
fruits = ["apple", "banana", "cherry"]
print(type(fruits))

# 6. Tuple
dimensions = (20, 40)
print(type(dimensions))

# 7. Set
unique_ids = {101, 102, 103}
print(type(unique_ids))

# 8. Dictionary
profile = {"name": "Shalini", "role": "Trainer"}
print(type(profile))

# 9. NoneType
result = None
print(type(result))

# 10. Complex number
z = 3 + 4j
print(type(z))


#  4. Operators – Arithmetic, Comparison, Logical

# 1. Arithmetic: Addition
print("Total:", 5 + 10)

# 2. Arithmetic: Subtraction
print("Remaining:", 20 - 6)

# 3. Arithmetic: Multiplication
print("Area:", 5 * 3)

# 4. Arithmetic: Division
print("Share per person:", 100 / 4)

# 5. Modulus: Find remainder
print("Remainder:", 10 % 3)

# 6. Comparison: Greater than
print("Is 10 greater than 5?", 10 > 5)

# 7. Comparison: Equal to
print("Is 7 equal to 7?", 7 == 7)

# 8. Logical: AND
print("Login:", True and False)

# 9. Logical: OR
print("Payment Success:", True or False)

# 10. Logical: NOT
print("User Active:", not False)


#  5. Escape Sequence – Handling special characters

# 1. New line
print("Hello\nWorld")

# 2. Tab space
print("Name:\tShalini")

# 3. Double quote inside string
print("She said, \"I love Python\"")

# 4. Single quote inside string
print('It\'s a sunny day')

# 5. Backslash in path
print("C:\\Users\\Shalini\\Documents")

# 6. Bell sound (if supported)
print("\a")

# 7. Carriage return
print("Start\rEnd")

# 8. Unicode character
print("Heart symbol: \u2764")

# 9. Octal value
print("\110\145\154\154\157")  # Prints Hello

# 10. Null character
print("End\0Start")  # \0 is null char, mostly invisible


# 6. Control Structures – If, if-else, elif, nested, etc.

# 1. Simple if
temp = 30
if temp > 25:
    print("It's hot outside.")

# 2. if-else
marks = 75
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# 3. elif
time = 12
if time < 12:
    print("Good morning")
elif time < 17:
    print("Good afternoon")
else:
    print("Good evening")

# 4. Nested if
age = 20
if age > 18:
    if age < 60:
        print("Eligible for job")

# 5. Check even/odd
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 6. Login simulation
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")

# 7. Grade system
score = 85
if score >= 90:
    print("A Grade")
elif score >= 70:
    print("B Grade")
else:
    print("C Grade")

# 8. Discount check
purchase = 1000
if purchase > 500:
    print("You get a discount!")

# 9. Age category
age = 4
if age < 5:
    print("Toddler")
elif age < 13:
    print("Child")
else:
    print("Teen or Adult")

# 10. Light switch
switch = False
if switch:
    print("Light is ON")
else:
    print("Light is OFF")
