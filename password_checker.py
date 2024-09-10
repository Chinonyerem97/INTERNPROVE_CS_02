import re

def check_password_strength(password):
    # Initialize strength indicators
    length_ok = len(password) >= 8
    starts_with_upper = password[0].isupper() if len(password) > 0 else False
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Calculate strength
    strength = 0
    if length_ok:
        strength += 2
    if starts_with_upper:
        strength += 2
    if has_lower:
        strength += 2
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    # Provide feedback
    feedback = []
    if not length_ok:
        feedback.append("Make sure your password is at least 8 characters long.")
    if not starts_with_upper:
        feedback.append("Your password must start with an uppercase letter.")
    if not has_lower:
        feedback.append("Include  at least one lowercase letter.")
    if not has_digit:
        feedback.append("Password should contain at least one digit.")
    if not has_special:
        feedback.append("Password should contain at least one special character.")
    
    # Determine overall strength
    if strength > 6:
        feedback.append("Password is very strong.")
    elif strength == 5:
        feedback.append("Password is moderate.")
    elif strength < 4:
        feedback.append("Password is weak.")
    else:
        feedback.append("Password is very weak.")

    return "\n".join(feedback)

# Welcome message
print("Welcome to Pamela's Password Strength Checker Tool!")

# Example usage
password = input("Kindly Enter Your Password: ")
print(check_password_strength(password))

