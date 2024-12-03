# **justInvest**

This assignment implements user authenticatoin and RBAC (Role based Access Control) to ensure users gain access to authorized controls based on their role

---
## **Main Features**

- **Role-Based Access Control (RBAC):** 
  - Access Privileges are based on specific roles (e.g., Client, Advisor, Admin).
  - User roles are assigned upon account creation, which determines their access control.

- **Secure Password Handling:**
  - Passwords are salted and hashed using bcrypt for enhanced security.
  - Password verification extracts the stored hash's salt and cost factor for comparison.
  - Passwords are stored in a separate file, not in plain text but hashed.
---

### **Prerequisites**

1. **Python 3.7 or later**
2. Install dependencies using pip (not required as VM already has it installed:
   ```bash
   pip install bcrypt

### **Run The code**
1. python main.py in terminal OR simply just run the main.py file 
2. Follow the prompts on the screen such as signing in/siging up and the assigned options for different roles.


### **Written and tested by Firas El-Ezzi 101239531**