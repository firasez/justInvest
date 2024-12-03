import bcrypt
from common import VALID_ROLES

def hash_password(password):
    """
    Add a salt to the password and hash it
    :param password: The password input by user during sign up
    :return: The value of the password after salting and hashing
    """

    password_bytes = password.encode('utf-8') #convert  to bytes
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt()) #generate and hash
    return hashed


def store_new_user(newUsername, newPassword, newRole):
    """
    Stores the new user's credintials in passwd.txt and people.txt.
    :param newUsername: The new username inputted during sign up
    :param newPassword: The new password inputted during sign up
    :param newRole: The role inputted during sign up
    :return: None
    """
    from Problem4 import logInUI # Local input to avoid circular imports

    # Hash the password using bcrypt
    hashedPassword = bcrypt.hashpw(newPassword.encode('utf-8'), bcrypt.gensalt())

    # Store username and the hashed password in the passwd.txt file
    with open("passwd.txt", "a") as passfile:
        passfile.write(f"{newUsername},{hashedPassword.decode('utf-8')}\n")

    # Store username, password, and role in people.txt (this file is mostly for testing and is needed for the role)
    with open("people.txt", "a") as peoplefile:
        peoplefile.write(f"{newUsername},{newPassword},{newRole}\n")

    print("Sign Up Successful!")
    logInUI()


def is_valid_username(username):
    """
    Checks if the username already exists during sign up
    :param username: The username inputted during sign up
    :return: False if username exists, True if else.
    """
    try:
        with open("people.txt", "r") as file:
            for line in file:
                # Get the current usernames stored in people.txt
                current_usernames, _, _ = line.strip().split(",")
                # Check if username already exists
                if current_usernames == username:
                    return False  # Username already exists
        return True  # Username does not exist
    except FileNotFoundError:
        print("Error: people.txt not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def is_valid_role(role):
    """
    Check if the role inputted by user during sign up is a valid role.
    :param role: Role inputted by user during sign up
    :return: True if role is valid, false if else
    """
    if role not in VALID_ROLES:
        print("Error: Role must be valid")
        return False
    return True




def check_list(username, password):
    """
    Checks if the username and password exist during sign in.
    It hashes the inputted password and compares it to the hashed passwords in the file to ensure security.
    :param username: The username input during sign in
    :param password: The password input during sign in
    :return: True if exists, false if else
    """
    try:
        with open('passwd.txt', 'r') as file:

            # Iterate thru every line in the txt file.
            for line in file:
                stored_username,stored_hash = line.strip().split(',')
                # Check if the username matches
                if username == stored_username:
                    # Compare the currently input password to the stored hash password
                    if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')): # Hashes the input and compares it's hash to the stored hash.
                        print(f"Welcome {stored_username}")
                        role = get_role_from_file(username, "people.txt")
                        if role:
                            print(f"You are now logged in as a {role}")
                        return True
                    else:
                        print("Incorrect password! Please try again.")
                        return False

            print("Incorrect username or password! Please try again.")
            return False
    except FileNotFoundError:
        print("The user data file 'passwd.txt' was not found.")
        return None


def get_role_from_file(username, file_path):
    """
    Fetches the role of the user,
    :param username: The user's username
    :param file_path: The file the users are stored in with their respective role
    :return: String: The user's role
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Fetch the
                stored_user, _, role = line.strip().split(',')
                if stored_user.strip() == username.strip():
                    return role.strip()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"
    return "Not found"