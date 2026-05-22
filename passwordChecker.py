import sys

#must contain 8 characters minimum.
def length_check():
    length = len(password)
    if length < 8:
        print('Result: Password must contain 8 or more characters')
    else:
       length_check == True

#at least 1 uppercase letter.
def upperCaseCondition():
    upper = any(char.isupper() for char in password)
    if not upper:
     print('Must include at least 1 upper case letter')
    else:
     upperCaseCondition == True


#at least 1 lowercase letter.
def lowerCaseCondition():
    lower = any(char.islower() for char in password)
    if not lower:
        print('Must include at least 1 lower case letter')
    else:
       lowerCaseCondition == True
#digits trigger else, not upper and lower case characters.
def numberCondition():
    number = any(char.isdigit() for char in password)
    if not number:
      print("Must include at least one number")
    else:
       numberCondition == True


     
while True:
 password = input('Password: ')
 length_check()
 upperCaseCondition()
 lowerCaseCondition()
 numberCondition()
 if numberCondition == True and lowerCaseCondition == True and upperCaseCondition == True and length_check == True:
    print("Strong password")
    break
          
 else:
    print("Weak password, try again")
