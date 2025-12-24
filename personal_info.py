# Personal Information Manager
# Author: Pavani Ravuvari
# Description: A beginner Python program to store, process,
# and display personal information using variables and user input.

# Welcome message
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Store static information
name = "Pavani Ravuvari"   # User's name
age = 20                  # User's age
city = "Guntur"           # User's city
hobby = "Learning Python" # User's hobby

# Get user input with validation
print("Please tell me about yourself:")
print("-" * 30)

favorite_food = input("What's your favorite food? ").strip()
while favorite_food == "":
    print("Food cannot be empty!")
    favorite_food = input("What's your favorite food? ").strip()

favorite_color = input("What's your favorite color? ").strip()
while favorite_color == "":
    print("Color cannot be empty!")
    favorite_color = input("What's your favorite color? ").strip()

# Calculate age in months
age_in_months = age * 12

# Display formatted output
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name           : {name.title()}")
print(f"Age            : {age} years ({age_in_months} months)")
print(f"City           : {city.title()}")
print(f"Hobby          : {hobby.capitalize()}")
print()
print(f"Favorite Food  : {favorite_food.capitalize()}")
print(f"Favorite Color : {favorite_color.capitalize()}")
print()

# Goodbye message
print("=" * 40)
print("Thank you for using the program!")
print("=" * 40)
