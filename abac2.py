def policy1():
 if (positions == "manager" and department == "accounting" and clearance_level == "high"):
  global access 
  access = "Access granted. Welcome, " + user_name + "."
  print(access)
 else:
  print("access denied")

#ABAC 
print("Enter your username:")
user_name = input()
print("Enter your position:")
positions = input().lower()
print("Enter your department:")
department = input().lower()
print("Enter your clearance level (high, medium, low):")
clearance_level = input().lower()
policy1()