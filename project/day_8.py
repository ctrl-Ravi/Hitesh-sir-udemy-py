"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""








import string
import random
import getpass

def check_password_strength(password):
    issues= []
    if len(password)< 8:
        issues.append("Too short (minimum 8 characters required)")
    if not any(c.islower() for c in password):
        issues.append(("missing lower case letter"))
    if not any(c.isupper() for c in password):
        issues.append(("missing Upper case letter"))
    if not any(c.isdigit() for c in password):
        issues.append(("missing Digit letter"))
    if not any(c in string.punctuation for c in password): # in punctuation all special character available
        issues.append(("missing a special letter"))
    return issues


def generate_strong_password(length=12):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    # chars_lower="abcdefgi" + "1234"+ "@!,."+"ABFDHWEI"
    return "".join(random.choice(chars) for _ in range(length))
    # return "".join(random.choice(chars_lower) for _ in range(length))

password= getpass.getpass("Enter a password")
issues = check_password_strength(password)

if not issues:
    print("Strong Password! You are good to go")
else:
    print("You got weak password")
    for issue in issues:
        print(f"- {issue}")

suggestion=generate_strong_password()

print("\n suggesting you a strong password")
print(suggestion)