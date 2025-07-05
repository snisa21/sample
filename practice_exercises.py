# Python Practice Exercises
# Complete these exercises to practice your Python skills

print("=== PYTHON PRACTICE EXERCISES ===\n")

# Exercise 1: Temperature Converter
print("Exercise 1: Temperature Converter")
print("Convert Celsius to Fahrenheit")
print("-" * 40)

def celsius_to_fahrenheit(celsius):
    # TODO: Write the formula to convert Celsius to Fahrenheit
    # Formula: (celsius * 9/5) + 32
    pass

# Test your function
test_celsius = 25
# result = celsius_to_fahrenheit(test_celsius)
# print(f"{test_celsius}°C = {result}°F")

print("\n" + "="*50 + "\n")

# Exercise 2: List Operations
print("Exercise 2: List Operations")
print("Find the sum of even numbers in a list")
print("-" * 40)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_even_numbers(number_list):
    # TODO: Write code to sum only the even numbers in the list
    pass

# Test your function
# result = sum_even_numbers(numbers)
# print(f"Sum of even numbers in {numbers}: {result}")

print("\n" + "="*50 + "\n")

# Exercise 3: String Manipulation
print("Exercise 3: String Manipulation")
print("Count vowels in a string")
print("-" * 40)

def count_vowels(text):
    # TODO: Write code to count vowels (a, e, i, o, u) in the text
    # Hint: Use a loop and check if each character is a vowel
    pass

# Test your function
test_text = "Hello World"
# vowel_count = count_vowels(test_text)
# print(f"Vowels in '{test_text}': {vowel_count}")

print("\n" + "="*50 + "\n")

# Exercise 4: Dictionary Operations
print("Exercise 4: Dictionary Operations")
print("Find the most frequent word")
print("-" * 40)

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

def most_frequent_word(word_list):
    # TODO: Write code to find the word that appears most frequently
    # Hint: Use a dictionary to count occurrences
    pass

# Test your function
# most_common = most_frequent_word(words)
# print(f"Most frequent word in {words}: {most_common}")

print("\n" + "="*50 + "\n")

# Exercise 5: Simple Calculator
print("Exercise 5: Simple Calculator")
print("Create a basic calculator")
print("-" * 40)

def calculator(num1, num2, operation):
    # TODO: Write code to perform basic operations (+, -, *, /)
    # Return the result of the operation
    pass

# Test your function
# print(calculator(10, 5, "+"))  # Should return 15
# print(calculator(10, 5, "-"))  # Should return 5
# print(calculator(10, 5, "*"))  # Should return 50
# print(calculator(10, 5, "/"))  # Should return 2.0

print("\n" + "="*50 + "\n")

# Exercise 6: Prime Number Checker
print("Exercise 6: Prime Number Checker")
print("Check if a number is prime")
print("-" * 40)

def is_prime(number):
    # TODO: Write code to check if a number is prime
    # A prime number is only divisible by 1 and itself
    pass

# Test your function
test_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in test_numbers:
#     if is_prime(num):
#         print(f"{num} is prime")
#     else:
#         print(f"{num} is not prime")

print("\n" + "="*50 + "\n")

# Exercise 7: Fibonacci Sequence
print("Exercise 7: Fibonacci Sequence")
print("Generate Fibonacci numbers")
print("-" * 40)

def fibonacci(n):
    # TODO: Write code to generate the first n Fibonacci numbers
    # Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
    pass

# Test your function
# fib_sequence = fibonacci(8)
# print(f"First 8 Fibonacci numbers: {fib_sequence}")

print("\n" + "="*50 + "\n")

# Exercise 8: Password Strength Checker
print("Exercise 8: Password Strength Checker")
print("Check password strength")
print("-" * 40)

def check_password_strength(password):
    # TODO: Write code to check password strength
    # Criteria: length >= 8, has uppercase, has lowercase, has digit
    # Return: "Weak", "Medium", or "Strong"
    pass

# Test your function
test_passwords = ["abc", "abc123", "Abc123", "Abc123!@#"]
# for pwd in test_passwords:
#     strength = check_password_strength(pwd)
#     print(f"Password '{pwd}': {strength}")

print("\n=== END OF EXERCISES ===")
print("Complete these exercises to practice your Python skills!")
print("Remove the 'pass' statements and implement each function.")
print("Uncomment the test lines to check your solutions.") 