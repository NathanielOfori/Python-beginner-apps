import re

def password_strength_checker(password):

    # checking and making sure there is at least one character in the password
    special_char = "!@#$%^&*+',/>.?{}[]()-=_:;`\""
    if not any(char in special_char for char in password):
        return False

    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    return True

while True:
    # displaying app name
    print("Welcome to the Password Strength Checker App")
    noct_password = input("Enter password: ")

    if password_strength_checker(noct_password):
        print("Nice! Your password is strong.")
        break
    else:
        print("Oh no! Your password is weak")
