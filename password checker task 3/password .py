import re

def check_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Criteria 1: Length of the password
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Criteria 2: Presence of uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Criteria 3: Presence of lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Criteria 4: Presence of numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Criteria 5: Presence of special characters
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine strength based on score
    if score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

# Get password input from the user
password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

# Output the results
print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for comment in feedback:
        print(f"- {comment}")