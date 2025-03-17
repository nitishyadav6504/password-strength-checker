import re

def check_password_strength(password):
    """
    Checks the strength of a password based on predefined criteria.
    Returns a strength rating.
    """
    strength = 0
    remarks = ""

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "❌ Password must be at least 8 characters long.\n"

    # Check for uppercase letter
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "❌ Add at least one uppercase letter (A-Z).\n"

    # Check for lowercase letter
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "❌ Add at least one lowercase letter (a-z).\n"

    # Check for digit
    if re.search(r"\d", password):
        strength += 1
    else:
        remarks += "❌ Add at least one digit (0-9).\n"

    # Check for special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks += "❌ Add at least one special character (e.g., @, #, $).\n"

    # Return strength rating
    if strength == 5:
        return "✅ Strong Password!", "Your password meets all requirements."
    elif strength >= 3:
        return "⚠️ Moderate Password", remarks
    else:
        return "❌ Weak Password!", remarks


if __name__ == "__main__":
    user_password = input("Enter your password: ")
    status, feedback = check_password_strength(user_password)
    print(f"\n{status}\n{feedback}")
