# Python Basics Tutorial
# This file contains examples of fundamental Python concepts

print("=== PYTHON BASICS TUTORIAL ===\n")

# 1. VARIABLES AND DATA TYPES
print("1. VARIABLES AND DATA TYPES")
print("-" * 30)

# Numbers
age = 25
height = 5.8
print(f"Age: {age} (integer)")
print(f"Height: {height} (float)")

# Strings
name = "Alice"
message = 'Hello, World!'
print(f"Name: {name} (string)")
print(f"Message: {message}")

# Boolean
is_student = True
is_working = False
print(f"Is student: {is_student} (boolean)")
print(f"Is working: {is_working}")

# Lists (mutable)
fruits = ["apple", "banana", "orange"]
print(f"Fruits list: {fruits}")

# Tuples (immutable)
coordinates = (10, 20)
print(f"Coordinates: {coordinates} (tuple)")

# Dictionaries
person = {
    "name": "Bob",
    "age": 30,
    "city": "New York"
}
print(f"Person dictionary: {person}")

print("\n" + "="*50 + "\n")

# 2. STRING OPERATIONS
print("2. STRING OPERATIONS")
print("-" * 30)

text = "Python Programming"
print(f"Original text: {text}")
print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"First word: {text.split()[0]}")

# String formatting
name = "John"
age = 25
print(f"{name} is {age} years old")
print("{} is {} years old".format(name, age))

print("\n" + "="*50 + "\n")

# 3. CONTROL STRUCTURES
print("3. CONTROL STRUCTURES")
print("-" * 30)

# If-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Score: {score}, Grade: {grade}")

# For loop
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

# While loop
print("\nCounting down from 3:")
count = 3
while count > 0:
    print(f"Count: {count}")
    count -= 1

print("\n" + "="*50 + "\n")

# 4. FUNCTIONS
print("4. FUNCTIONS")
print("-" * 30)

# Simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Function with default parameter
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))
print(greet_with_title("Johnson", "Dr."))

print("\n" + "="*50 + "\n")

# 5. LISTS AND LIST OPERATIONS
print("5. LISTS AND LIST OPERATIONS")
print("-" * 30)

numbers = [1, 2, 3, 4, 5]
print(f"Original list: {numbers}")

# Adding elements
numbers.append(6)
print(f"After append: {numbers}")

numbers.insert(0, 0)
print(f"After insert: {numbers}")

# Removing elements
numbers.remove(3)
print(f"After removing 3: {numbers}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

print("\n" + "="*50 + "\n")

# 6. ERROR HANDLING
print("6. ERROR HANDLING")
print("-" * 30)

# Try-except block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred")
finally:
    print("This always executes")

print("\n" + "="*50 + "\n")

# 7. FILE HANDLING
print("7. FILE HANDLING")
print("-" * 30)

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file!\n")
    file.write("This is the second line.")

print("Created sample.txt file")

# Reading from a file
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(f"File content:\n{content}")
except FileNotFoundError:
    print("File not found!")

print("\n" + "="*50 + "\n")

# 8. PRACTICE EXERCISES
print("8. PRACTICE EXERCISES")
print("-" * 30)

# Exercise 1: Calculate average
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

test_scores = [85, 90, 78, 92, 88]
average = calculate_average(test_scores)
print(f"Test scores: {test_scores}")
print(f"Average score: {average:.2f}")

# Exercise 2: Find maximum number
def find_max(numbers):
    if len(numbers) == 0:
        return None
    return max(numbers)

max_score = find_max(test_scores)
print(f"Highest score: {max_score}")

print("\n=== END OF TUTORIAL ===")
print("Practice these concepts and experiment with the code!") 