grades = []

print("Welcome to the Grade Calculator!")
while True:
 print("Would you like to enter a grade? (yes/no) ")
 answer = input()

 if answer.lower() == "yes":
   print("enter your grade: ")
   try:
        score = float(input())
        grades.append(score)
        if score < 0 or score> 100:
                print("Please enter a number between 0 and 100")
        elif score <= 59:
                print("Failed test")
        elif score <= 62:
                print("You got a D-")
        elif score <= 66:
                print("You got a D")
        elif score <= 69:
                print("You got a D+")
        elif score <= 72:
                print("You got a C-")
        elif score <= 76:
                print("You got a C")
        elif score <= 79:
                print("You got a C+")
        elif score <= 82:
                print("You got a B-")
        elif score <= 86:
                print("You got a B")
        elif score <= 89:
                print("You got a B+")
        elif score <= 92:
                print("You got a A-")
        elif score <= 96:
                print("You got a A")
        else:
                print("You got a A+")
   except ValueError:
            print("Invalid input, please enter a number between 0 and 100")
            continue

 if answer.lower() == "no":
        print("Would you like to see all your grades? (yes/no) ")
        response = input()
        if response.lower() == "yes":
            print("Your grades are: " + str(grades))
            break

        else:
                response.lower() == "no"
                print("Goodbye!")
                break
