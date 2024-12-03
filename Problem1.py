from common import ROLES_MENU


# Access Conntrol Mechanism RBAC
def display_special_UI(role):
    from Problem4 import logInUI # local import to avoid circular import
    """
    Using DMAC, it properly displays the different specific UI for different roles
    :param role: The user's role
    :return: None
    """

    #Check if role exist
    if role in ROLES_MENU:
        print(f"Here are your options, {role}:")
        # Enumerate the special options for the specific role
        for i, option in enumerate(ROLES_MENU[role], start=1):
            print(f"{i}. {option}")

        count = len(ROLES_MENU[role])  # Total number of options

        while True:
            try:
                user_input = int(input("Please enter your option: "))
                if 0 < user_input <= count:
                    selected_option = ROLES_MENU[role][user_input - 1] # Go to the last index of the options which is always Log out
                    if selected_option == "Log out":
                        print("Logging out...")
                        logInUI()
                    else:
                        print("Access Granted to "+ selected_option)
                        display_special_UI(role)
                    break
                else:
                    print("Invalid option! Please try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")
    else:
        print("Role does not exist.")
