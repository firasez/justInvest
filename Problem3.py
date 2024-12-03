from Problem2 import store_new_user, is_valid_role, is_valid_username
from common import WEAK_PASSWORDS
import re

def sign_up_UI():
    """
    User interface for signing up
    :return: None
    """
    while True:
        newUsername = input("Create username: ")
        newPassword = input("Create password: ")
        newRole = input("Enter role: ")


        if not is_valid_username(newUsername):
            print("Username already exists. Please try again with a different username")
            continue
        if not is_valid_password(newUsername, newPassword):
            print("Please try again with a valid password.")
            continue

        if not is_valid_role(newRole):
            print("Please try again with a valid role")
            continue

        store_new_user(newUsername, newPassword, newRole)
        break

def is_valid_password(username, password):
    """
    Validates a password based on given requirements.


    :param username: The username (str).
    :param password: The password to validate (str).
    :return: A tuple (is_valid, message) where is_valid is True/False, and message explains why.
    """
    # Check password length
    if not (8 <= len(password) <= 12):
        print("Error: Password must be between 8 and 12 characters long.")
        return False

    # Check for at least one upper-case letter
    if not re.search(r"[A-Z]", password):
        print("Error: Password must include at least one upper-case letter.")
        return False

    # Check for at least one lower-case letter
    if not re.search(r"[a-z]", password):
        print("Error: Password must include at least one lower-case letter.")
        return False

    # Check for at least one numerical digit
    if not re.search(r"\d", password):
        print("Error: Password must include at least one numerical digit.")
        return False

    # Check for at least one special character
    if not re.search(r"[!@#$%*&]", password):
        print("Error: Password must include at least one special character (!, @, #, $, %, *, &).")
        return False

    # Check if the password is in the weak passwords list
    if password.lower() in WEAK_PASSWORDS:
        print("Error: Password is too weak or commonly used.")
        return False

    # Check if the password matches the username
    if password.lower() == username.lower():
        print("Error: Password must not match the username.")
        return False

    # All checks passed
    return True