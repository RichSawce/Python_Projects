#must contain 8 characters minimum.
def length_check(password):
    length = len(password)
    if length < 8:
        print('Result: Password must contain 8 or more characters')
        return False
    else:
        return True

#at least 1 uppercase letter.
def upperCaseCondition(password):
    upper = any(char.isupper() for char in password)
    if not upper:
     print('Must include at least 1 upper case letter')
    else:
     return True

#at least 1 lowercase letter.
def lowerCaseCondition(password):
    lower = any(char.islower() for char in password)
    if not lower:
        print('Must include at least 1 lower case letter')
    else:
       return True

#digits trigger else, not upper and lower case characters.
def numberCondition(password):
    number = any(char.isdigit() for char in password)
    if not number:
      print("Must include at least one number")
    else:
       return True

while True:
 password = input('Password: ')
 has_length = length_check(password)
 has_upper = upperCaseCondition(password)
 has_lower = lowerCaseCondition(password)
 has_number = numberCondition(password)
 if has_length and has_upper and has_lower and has_number:
    print("Strong password")
    break
          
 else:
    print("Weak password, try again")

