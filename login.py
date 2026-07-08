import csv
import os
import re

class Login():
    def __init__(self,name,username,password)
        self.name=name
        self.user_name=user_name
        self.password=password

def name():
    self.name=input("Please enter your name: ")

def user_name():
    self.user_name=input("Please enter your username: ")

FILE_NAME = "users.csv"

# Create the CSV file with headings if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Username", "Password"])

def check_password(password):
    """Checks if the password meets the requirements."""

    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"\d", password):
        return False, "Password must contain at least one number."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, "Password is valid."


def username_exists(username):
    """Checks whether the username already exists."""

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Username"] == username:
                return True
    return False

#Call Function
def register():
    """
    CALL userManager.py()
    """Registers a new user."""
    print("\n===== REGISTER =====")
    name = input("Enter your name: ")
    while True:
        username = input("Enter a username: ")

        if username_exists(username):
            print("Username already exists. Please choose another.")
        else:
            break

    while True:
        password = input("Create a password: ")

        valid, message = check_password(password)

        if valid:
            break

        print(message)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, username, password])

    print("\nRegistration successful!")
"""