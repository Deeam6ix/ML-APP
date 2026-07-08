# Minimal user registration and login module.
# Uses a CSV file for storage and regex for password validation.

import csv
import os
import re

# CSV file name (global)
USER_FILE = 'users.csv'

# Password regex: at least 8 chars, upper, lower, digit, special
PASSWORD_PATTERN = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!])[A-Za-z\d@#$%^&+=!]{8,}$'
)


def _ensure_file():
    # Create the CSV file and name it if it doesn't exist.
    if not os.path.isfile(USER_FILE):
        with open(USER_FILE, 'w', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(['name', 'username', 'password'])


def _read_users():
    # Return list of user dicts from CSV.
    _ensure_file()
    with open(USER_FILE, 'r', newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def _write_users(users):
    # Write list of user dicts to CSV (overwrites).
    with open(USER_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'username', 'password'])
        writer.writeheader()
        writer.writerows(users)


def validate_password(password):
    # Return True if password meets strength requirements.
    return bool(PASSWORD_PATTERN.match(password))


def register_user(name, username, password):

    # Register a new user.
    # Returns (success, message).

    if not validate_password(password):
        return False, ("Password must be 8+ chars, include upper, lower, digit, "
                       "and special (@#$%^&+=!).")

    users = _read_users()
    if any(u['username'] == username for u in users):
        return False, "Username already exists."

    users.append({'name': name, 'username': username, 'password': password})
    _write_users(users)
    return True, "User registered."


def login_user(username, password):
   
    # Verify login credentials.
    # Returns (success, message).
   
    users = _read_users()
    for u in users:
        if u['username'] == username:
            if u['password'] == password:
                return True, f"Welcome, {u['name']}!"
            return False, "Incorrect password."
    return False, "Username not found."


def user_exists(username):
    # Return True if username is already taken.
    users = _read_users()
    return any(u['username'] == username for u in users)