import sys
import time


def d_email():
    print("Accessing Diamond Email...")
    time.sleep(1)
    print("Want to access another application? Type 'yes' to continue or 'no' to exit.")
    user_input = input()
    while True:
        if user_input.lower() == "no":
            print("logging out...")
            sys.exit()
        else:
            print("Returning to application menu...")
            return


def d_drive():
    print("Accessing Diamond Drive...")
    time.sleep(1)
    print("Want to access another application? Type 'yes' to continue or 'no' to exit.")
    user_input = input()
    while True:
        if user_input.lower() == "no":
            print("logging out...")
            sys.exit()
        else:
            print("Returning to application menu...")
            return


def d_messenger():
    print("Accessing Diamond Messenger...")
    time.sleep(1)
    print("Want to access another application? Type 'yes' to continue or 'no' to exit.")
    user_input = input()
    while True:
        if user_input.lower() == "no":
            print("logging out...")
            sys.exit()
        else:
            print("Returning to application menu...")
            return


password = []  # starts empty
while True:
    user_input = input("Welcome to Diamond Enterprises\n"
                       "Before accessing our services, please create your password or type 'quit' to exit\n")
    if user_input.lower() == "quit":
        print("logging out...")
        sys.exit()
    else:
        password.append(user_input)
        print("your password is: ", password)
        break
print("please enter your password to continue:")
input_password = input()
if input_password != password[0]:
    print("incorrect password, exiting...")
    sys.exit()
else:
    print("access granted")
while True:
    print("Which application would you like to access?\n"
          "Diamond Email\n"
          "Diamond Drive\n"
          "Diamond Messenger\n")
    user_input = input()
    while True:
        if user_input == "Diamond Email":
            d_email()
            break

        if user_input == "Diamond Drive":
            d_drive()
            break
        if user_input == "Diamond Messenger":
            d_messenger()
            break
        elif user_input != ("diamond email", "diamond drive", "diamond messenger"):
         while True:
            print("Invalid application name, try again or type 'quit' to exit: \n")
            if user_input.lower() == "quit":
                print("logging out...")
                sys.exit()
            else:
                break
