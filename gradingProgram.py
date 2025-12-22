print("enter your grade: ")
try:
    score = float(input())
    if score < 0 or score> 100:
            print("Please enter a number between 0 and 100")
    elif score <= 50:
            print("Failed test")
    elif score <= 70:
            print("You got a C")
    elif score <= 85:
            print("You got a B")
    elif score > 85:
        print("Congratulations, you got an A!")
except ValueError:
        print("Invalid input, please enter a number between 0 and 100")
