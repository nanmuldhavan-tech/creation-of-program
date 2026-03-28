import re

def check_password_strength(password):
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Uppercase check
    if re.search("[A-Z]", password):
        strength += 1

    # Lowercase check
    if re.search("[a-z]", password):
        strength += 1

    # Digit check
    if re.search("[0-9]", password):
        strength += 1

    # Special character check
    if re.search("[@#$%^&+=!]", password):
        strength += 1

    # Result
    if strength == 5:
        return "Strong Password 🔐"
    elif strength >= 3:
        return "Medium Password ⚠️"
    else:
        return "Weak Password ❌"

# Input from user
password = input("Enter your password: ")
result = check_password_strength(password)

print("Password Strength:", result)
