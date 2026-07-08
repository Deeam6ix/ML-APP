2.  Functions
    
    _ensure_file()
        Internal helper: creates the CSV file with the name users.csv row if it doesn’t exist.

    _read_users() -> list of dicts
        Reads all user records from the CSV and returns them as a list of dictionaries.
        Each dict has keys: 'name', 'username', 'password'.

    _write_users(users)
        Writes the entire list of user dictionaries back to the CSV, overwriting the file.

      validate_password(password) -> bool
        Checks if the password matches the regex pattern:
            • At least 8 characters
            • At least one uppercase letter (A-Z)
            • At least one lowercase letter (a-z)
            • At least one digit (0-9)
            • At least one special character from: @#$%^&+=!

    - register_user(name, username, password) -> (bool, str)
        Attempts to register a new user.
        Steps:
          1. Validate the password.
          2. Check if the username already exists (by reading the CSV).
          3. If both pass, append the new user record to the CSV.
        Returns (True, "User registered.") on success, or (False, error_message).

    - login_user(username, password) -> (bool, str)
        Verifies credentials.
        Reads the CSV and compares username/password.
        Returns (True, welcome_message) if successful, else (False, error_message).

    - user_exists(username) -> bool
        Convenience function to test whether a username is already taken.