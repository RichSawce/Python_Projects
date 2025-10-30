import random
import sys
import time
import string



def d_email():
    print("checking token validity...")
    time.sleep(1)
    if token is None and "email.read" in permissions:
        print("invalid token, logging out...")
        sys.exit()
    else:
     print(user_name, "'s token is valid.")
     time.sleep(1)
     print("Accessing Diamond Email...")
     time.sleep(1)
     print("Want to access another application? Type 'yes' to continue or 'no' to exit.")
     user_input = input()
     while True:
        if user_input.lower() == "no":
            print("logging out...")
            sys.exit()
        if user_input.lower() == "yes":
            print("Returning to application menu...\n")
            time.sleep(1)
            return
        elif user_input.lower() != ("yes", "no"):
            print("command not recognized, Type 'yes' to continue or 'no' to exit.\n")
            user_input = input()


def d_drive():
    print("checking token validity...")
    time.sleep(1)
    if token is None and "email.read" in permissions:
        print("invalid token, logging out...")
        sys.exit()
    else:
     print(user_name, "'s token is valid.")
     time.sleep(1)
     print("Accessing Diamond Drive...")
     time.sleep(1)
     print("Want to access another application? Type 'yes' to continue or 'no' to exit.")
     user_input = input()
     while True:
        if user_input.lower() == "no":
            print("logging out...")
            sys.exit()
        if user_input.lower() == "yes":
            print("Returning to application menu...\n")
            time.sleep(1)
            return
        elif user_input.lower() != ("yes", "no"):
            print("command not recognized, Type 'yes' to continue or 'no' to exit.\n")
            user_input = input()


def d_messenger():
    print("checking token validity...")
    time.sleep(1)
    if token is None and "email.read" in permissions:
        print("invalid token, logging out...")
        sys.exit()
    else:
     print(user_name, "'s token is valid.")
     time.sleep(1)
     print("Accessing Diamond Messenger...")
     time.sleep(1)
     print("Want to access another application? Type 'yes' to continue or 'no' to exit.")
     user_input = input()
     while True:
        if user_input.lower() == "no":
            print("logging out...")
            sys.exit()
        if user_input.lower() == "yes":
            print("Returning to application menu...\n")
            time.sleep(1)
            return
        elif user_input.lower() != ("yes", "no"):
            print("command not recognized, Type 'yes' to continue or 'no' to exit.\n")
            user_input = input()

class Token:
    def __init__(self, user_name, session_ID, permissions):
        self.user_name = user_name
        self.session_ID = session_ID
        self.permissions = permissions
        self.readEmail = "email.read" in self.permissions
        self.readDrive = "drive.read" in self.permissions
        self.readMessenger = "messenger.read" in self.permissions

    def display_info(self):
        print("Token Information:")
        print("User Name:", self.user_name)
        print("Session ID:", self.session_ID)
        print("Permissions:", ", ".join(self.permissions))
        

    

session_ID = []  # starts empty
password = []  # starts empty
permissions = [
    "email.read",
    "drive.read",
    "messenger.read"
]

#enter name
user_name = input("Please enter your username: ")

while True:
    user_input = input("Hi " + user_name + ", welcome to Diamond Enterprises\n"
                       "Before accessing our services, please create your password or type 'quit' to exit\n")
    if user_input.lower() == "quit":
        print("logging out...")
        sys.exit()
    else:
        # create password
        password.append(user_input)
        char_length = len(7 * user_input)
        # Define the possible characters for the random string
        possible_characters = string.ascii_letters + string.digits + string.punctuation
        # Generate a random string
        randomized_text = "".join(random.choice(possible_characters) for _ in range(char_length))
        print("your password has been encrypted: ", randomized_text)
        break
        
print("please enter your password to continue:")
input_password = input()
#failed password check
if input_password != password[0]:
    print("incorrect password, exiting...")
    sys.exit()
#successful password check
else:
    print("access granted")
    time.sleep(1)
    print("generating session token...")
    # create session token
    session_ID.append(random.randint(100000, 999999))
    print(user_name + " ,your session token is: ", session_ID[0])
    time.sleep(1)
    print("Session token generated.\n")
    time.sleep(1)
token = Token(user_name, session_ID, permissions)
token.display_info()
while True:
    print("Which application would you like to access?\n"
          "Diamond Email\n"
          "Diamond Drive\n"
          "Diamond Messenger\n")
    user_input = input()
    while True:
        if user_input == "Diamond Email" and token.readEmail:
            d_email()
            break
        if user_input == "Diamond Drive" and token.readDrive:
            d_drive()
            break
        if user_input == "Diamond Messenger" and token.readMessenger:
            d_messenger()
            break
        elif user_input != ("diamond email", "diamond drive", "diamond messenger"):
         
            print("Invalid application name, try again or type 'quit' to exit: \n")
            if user_input.lower() == "quit":
                print("logging out...")
                sys.exit()
            else:
                break
