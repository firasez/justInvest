from Problem3 import sign_up_UI
from Problem2 import check_list,get_role_from_file
from  Problem1 import display_special_UI


def logInUI():
    print("Welcome to justInvest!")
    print("------------------------")
    print("1. Sign In (Already have an account)\n"
          "2. Sign Up (Create a new account)\n")

    inp = input("Enter: ")
    if inp == "1":
        justInvestUI()
    elif inp == "2":
        sign_up_UI()
    else:
        print("Invalid option! Please try again")
        logInUI()

def justInvestUI():
    """
    The basic justInvest UI with all possible options after sign in.
    :return: None
    """
    print("justInvest System")
    print("------------------------")
    print("Operations available on the system")
    print("1. View account balance\n"
          "2. View investment portfolio\n"
          "3. Modify investment portfolio\n"
          "4. View Financial Advisor contact info\n"
          "5. View Financial Planner contact info\n"
          "6. View money market insurance\n"
          "7. View private consumer instruments\n")

    sign_in_UI()


def sign_in_UI():
    """
    Sign in UI used in justInvestUI
    :return: None
    """
    username = input("Enter username: ")
    password = input("Enter password: ")

    while True:
        if (check_list(username, password)):
            display_special_UI(get_role_from_file(username, "people.txt"))

        else:
            justInvestUI()
        break


def is_valid_username(username):
    """
    Checks if username already exists during sign up
    :param username: The username inputted during sign up
    :return: False if username exists, true else if
    """

    try:
        with open("people.txt", "r") as file:
            for line in file:
                #Iterate and split by commas
                existing_username, _, _ = line.strip().split(",")
                # Check if the username matches any existing username
                if existing_username == username:
                    return False  # Username already exists
        return True  # Username does not exist
    except FileNotFoundError:
        print("Error: people.txt not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False