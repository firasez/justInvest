# A list of weak passwords found online
WEAK_PASSWORDS = {
    "123456", "password", "123456789", "12345", "1234", "qwerty", "abc123", "password1", "letmein",
    "welcome", "monkey", "iloveyou", "123123", "admin", "qwerty123", "sunshine", "123qwe", "qwertyuiop",
    "123321", "1q2w3e4r", "1234qwer", "qwerty1", "1qaz2wsx", "letmein123", "password123", "football",
    "dragon", "123abc", "1password", "qwerty1", "letmein1234", "hello123", "welcome1", "welcome123",
    "password1!", "iloveyou123", "qwerty@123", "123qweasd", "superman", "iloveyou1", "1234abcd",
    "qwertyqwerty", "qwerty12345", "password1234", "12345678a", "password!@#", "trustno1", "abc12345",
    "password123!", "letmein123!", "letmein1", "qwerty1234", "1234567a", "123abc456", "admin123",
    "12345qwerty", "chicken", "starwars", "welcome1!", "monkey123", "qwertyuiop123", "12345abc",
    "abcdef", "super123", "112233", "passw0rd", "12345a", "qwerty@1", "password1abc", "letmein!@#",
    "passw0rd123", "shadow", "freedom", "qwerty!@#", "admin1", "iloveu", "test123", "passwordtest",
    "1a2b3c4d", "god123", "testpassword", "root", "12341234", "blue123", "qwertyy", "baseball",
    "1q2w3e4r5t", "princess", "123abcd", "qwerty789", "123pass", "abc12345", "abcdef123", "loveyou123",
    "letmeinqwerty", "test1", "123test", "monkey1", "qwerty321", "123qwerty", "pass123", "qwert123",
    "mypassword", "qwertyzxcvbn", "1password123", "qwerty12", "passwordq1", "test1234", "password12",
    "letmeinagain", "qwerty098", "1a2b3c4d5e", "iloveyou1234", "password123q", "apple123", "welcome1!",
    "1q2w3e4r5t6y", "1234abcd1234", "monkey1!", "abc@123", "password2", "iloveu1234", "1234password",
    "iloveyou@1", "123!qwerty", "password1234!", "mypass123", "admin@123", "adminpass", "12345hello",
    "lovely123", "sunshine123", "hello1234", "password789", "qwerty&123", "loveme123", "12345hello!",
    "1a2b3c4d5f", "passw0rd1", "mysecurepassword", "abcdefgh", "password1!", "rocky123", "trustme123",
    "jessica", "liverpool", "coolpass123", "qwerty4444", "abc@def123"
}

# A list of all valid roles to ensure users cannot sign up with anything else
VALID_ROLES = {"Client", "Premium Client", "Financial Advisor", "Financial Planner", "Teller"}

#Each role has its respective UI, using RBAC
ROLES_MENU = {
    "Client": ["View account balance", "View investment portfolio", "View Finanical Advisor contact info", "Log out"],
    "Premium Client": ["View account balance", "View investment portfolio", "View Finanical Advisor contact info",
                       "Modify investment portfolio", "View Finanical Planner contact", "Log out"],
    "Financial Advisor": ["View Client's account balance", "View Client's investment portfolio",
                          "Modify Client's investment portfolio", "View private consumer instruments", "Log out"],
    "Financial Planner": ["View Client's account balance", "View Client's investment portfolio",
                          "Modify Client's investment portfolio", "View money market instruments",
                          "View private consumer instruments", "Log out"],
    "Teller": ["View Client's account balance", "View Client's investment portfolio", "Log out"],
}