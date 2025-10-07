import sys

#User Accounts
Bob = "Name: Bob\n" \
"DOB: 12/03/85\n"
"Balance: $300"
Alice = "Name: Alice\n" \
"DOB: 05/17/00\n"
"Balance: $5000"
Xi = "Name: Xi\n" \
"DOB: 02/08/95\n"
"Balance: $2800"
Marcus = "Name: Marcus\n" \
"DOB: 07/15/93\n"
"Balance: $10,975"

audit = "2025-10-06T07:12:03Z server1 kernel: [    0.000000] Booting Linux on physical CPU 0x0\n" \
"2025-10-06T07:12:05Z server1 systemd[1]: Started Journal Service.\n" \
"2025-10-06T07:12:06Z server1 NetworkManager[814]: <info>  [2025-10-06T07:12:06Z] device (eth0): state change: unmanaged -> unavailable (reason 'managed', sys-iface-state: 'external')\n" \
"2025-10-06T07:12:08Z server1 sshd[1023]: Server listening on 0.0.0.0 port 22.\n" \
"2025-10-06T07:12:09Z server1 sshd[1023]: Server listening on :: port 22.\n" \
"2025-10-06T07:12:15Z server1 CRON[1234]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)\n" \
"2025-10-06T07:15:01Z server1 rsyslogd: [origin software="'rsyslogd" swVersion="8.2102.0" x-pid="987" x-info="https://www.rsyslog.com'"] rsyslogd was HUPed\n" \
"2025-10-06T08:02:41Z server1 sshd[2045]: Accepted publickey for alice from 198.51.100.23 port 54812 ssh2: RSA SHA256:AbCdEfGh..."



#Roles
def user():
  print("Would you like to view your account?")
  while True:
   if input() == "yes":
     print("your account balance:\n $5000")
     
   elif input() == "no":
    print("Would you like to make a transfer?")
    while True:
     if input() == "yes": print("sending funds to Bob")
   
     elif input() == "no": print("Have a good day!")
  

     sys.exit()
 
   

def CS():
  print("Enter the name of the customer to view their account:\n" \
  "Bob, Alice, Xi, Marcus, or type 'exit' to leave")
  input()
  while True:
   if input == "Bob": print(Bob)
   elif input == "Alice": print(Alice)
   elif input == "Xi": print(Xi)
   elif input == "Marcus": print(Marcus)
   elif "exit": print("Goodbye!")
   sys.exit()
   break
  return

def admin():
  print("What would you like to do?\n" \
  "view logs?\n" \
  "update accounts?\n" \
  "manage system?")
  while True:
    if input == "view logs": print(audit)
    elif input == "update accounts": print("accounts updating.....")
    elif input == "manage system": print("access denied, must be senior admin")
    elif input != "view logs" or "update accounts" or "manage system":
      return



input("Enter your role:\n")
role = "User" or "Customer Service" or "Administrator" or "Auditor"
while True:
 if role == "User":
   user()
 elif role == "Customer Service":
   CS("Good day\n")
 elif role == "Administrator":
   admin("Becareful, you got the power!")
   break


