import random 
import sys

#User Accounts
Bob = "\nName: Bob\n" \
"DOB: 12/03/85\n" \
"Balance: $300"
Alice = "\nName: Alice\n" \
"DOB: 05/17/00\n" \
"Balance: $5000"
Xi = "\nName: Xi\n" \
"DOB: 02/08/95\n" \
"Balance: $2800"
Marcus = "\nName: Marcus\n" \
"DOB: 07/15/93\n" \
"Balance: $10,975"

#audit logs
audit = "\n2025-10-06T07:12:03Z server1 kernel: [    0.000000] Booting Linux on physical CPU 0x0\n" \
"2025-10-06T07:12:05Z server1 systemd[1]: Started Journal Service.\n" \
"2025-10-06T07:12:06Z server1 NetworkManager[814]: <info>  [2025-10-06T07:12:06Z] device (eth0): state change: unmanaged -> unavailable (reason 'managed', sys-iface-state: 'external')\n" \
"2025-10-06T07:12:08Z server1 sshd[1023]: Server listening on 0.0.0.0 port 22.\n" \
"2025-10-06T07:12:09Z server1 sshd[1023]: Server listening on :: port 22.\n" \
"2025-10-06T07:12:15Z server1 CRON[1234]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)\n" \
"2025-10-06T07:15:01Z server1 rsyslogd: [origin software="'rsyslogd" swVersion="8.2102.0" x-pid="987" x-info="https://www.rsyslog.com'"] rsyslogd was HUPed\n" \
"2025-10-06T08:02:41Z server1 sshd[2045]: Accepted publickey for alice from 198.51.100.23 port 54812 ssh2: RSA SHA256:AbCdEfGh...\n"

audit_alice = "\n2025-10-06T06:58:12Z server1 kernel: [    0.000000] CPU0: microcode updated early to revision 0x1a\n" \
"2025-10-06T06:58:14Z server1 systemd[1]: Reached target Basic System.\n" \
"2025-10-06T06:58:20Z server1 NetworkManager[814]: <info>  [2025-10-06T06:58:20Z] device (eth0): state change: unavailable -> activated (reason 'now managed', sys-iface-state: 'external')\n" \
"2025-10-06T07:01:49Z server1 sshd[1987]: Accepted publickey for alice from 198.51.100.23 port 52134 ssh2: RSA SHA256:Al1cEKey...\n" \
"2025-10-06T07:01:50Z server1 systemd-logind[412]: New session 12 of user alice.\n" \
"2025-10-06T07:03:12Z server1 sudo:     alice : TTY=pts/3 ; PWD=/home/alice ; USER=root ; COMMAND=/usr/bin/apt update\n" \
"2025-10-06T07:03:13Z server1 apt[2041]: Get:1 http://archive.ubuntu.com/ubuntu focal InRelease [265 kB]\n" \
"2025-10-06T07:10:00Z server1 cron[2234]: (alice) CMD ( /usr/local/bin/daily-checks --send-report )\n"

audit_bob = "\n2025-10-06T07:05:00Z server1 systemd[1]: Starting Daily apt download activities.\n" \
"2025-10-06T07:05:02Z server1 rsyslogd: [origin software='rsyslogd' swVersion='8.2102.0' x-pid='987' x-info='https://www.rsyslog.com'] rsyslogd started\n" \
"2025-10-06T07:07:51Z server1 sshd[2178]: Failed password for bob from 203.0.113.45 port 60211 ssh2\n" \
"2025-10-06T07:07:53Z server1 sshd[2178]: Received disconnect from 203.0.113.45: 11: Bye Bye [preauth]\n" \
"2025-10-06T07:09:24Z server1 sshd[2250]: Accepted password for bob from 192.0.2.11 port 54122 ssh2\n" \
"2025-10-06T07:09:25Z server1 systemd-logind[412]: New session 13 of user bob.\n" \
"2025-10-06T07:12:02Z server1 sudo:     bob : TTY=pts/4 ; PWD=/home/bob ; USER=root ; COMMAND=/usr/bin/systemctl status nginx\n" \
"2025-10-06T07:12:03Z server1 systemd[1]: nginx.service: Found left-over process 3199 (nginx) in control group while starting unit. Cleaning up.\n"

audit_xi = "\n2025-10-06T07:20:11Z server1 kernel: [  120.123456] usb 1-1.2: new high-speed USB device number 4 using xhci_hcd\n" \
"2025-10-06T07:20:13Z server1 systemd[1]: Started Session 14 of user xi.\n" \
"2025-10-06T07:21:34Z server1 sshd[2456]: Accepted publickey for xi from 198.51.100.77 port 60200 ssh2: ECDSA SHA256:Xi...\n" \
"2025-10-06T07:22:01Z server1 sudo:     xi : TTY=pts/5 ; PWD=/home/xi ; USER=root ; COMMAND=/usr/bin/journalctl -u database.service\n" \
"2025-10-06T07:22:02Z server1 database[3190]: [INFO] 2025-10-06T07:22:02Z - Starting shard sync (shard=3)\n" \
"2025-10-06T07:22:08Z server1 database[3190]: [ERROR] 2025-10-06T07:22:08Z - shard sync failed: timeout contacting peer 10.0.0.7\n" \
"2025-10-06T07:25:00Z server1 scp[2524]: xi@198.51.100.77: /home/xi/backup.sql -> /var/backups/xi/backup.sql\n" \
"2025-10-06T07:30:00Z server1 logrotate[2578]: error: error running shared postrotate script for '/var/log/database/*.log'\n"

audit_marcus = "\n2025-10-06T07:35:00Z server1 systemd[1]: Starting Daily cleanup of temp files.\n" \
"2025-10-06T07:35:02Z server1 tmpreaper[2621]: Cleaning /tmp (maxage=3d, subdirs=yes)\n" \
"2025-10-06T07:36:18Z server1 sshd[2710]: Accepted publickey for marcus from 203.0.113.12 port 52900 ssh2: RSA SHA256:M@rcUsKey...\n" \
"2025-10-06T07:36:19Z server1 systemd-logind[412]: New session 15 of user marcus.\n" \
"2025-10-06T07:38:05Z server1 sudo:     marcus : TTY=pts/6 ; PWD=/home/marcus ; USER=root ; COMMAND=/usr/bin/tail -n 200 /var/log/nginx/access.log\n" \
"2025-10-06T07:40:12Z server1 nginx[3199]: 192.0.2.200 - marcus [06/Oct/2025:07:40:12 +0000] \"POST /api/v2/upload HTTP/1.1\" 201 1024 \"-\" \"python-requests/2.31.0\"\n" \
"2025-10-06T07:42:33Z server1 fail2ban.actions[4250]: NOTICE  [sshd] Ban 198.51.100.99\n" \
"2025-10-06T07:45:00Z server1 backup[3001]: Completed incremental backup for /home/marcus -> /mnt/backup/2025-10-06/marcus/ (1.8G transferred)\n"

audit_custserv = "\n2025-10-06T08:42:00Z server2 systemd[1]: Started Journal Service.\n" \
"2025-10-06T08:42:02Z server2 NetworkManager[734]: <info>  [2025-10-06T08:42:02Z] device (eth1): state change: unmanaged -> unavailable (reason 'managed')\n" \
"2025-10-06T08:42:05Z server2 sshd[1011]: Server listening on 0.0.0.0 port 22.\n" \
"2025-10-06T08:42:05Z server2 sshd[1011]: Server listening on :: port 22.\n" \
"2025-10-06T08:45:18Z server2 sshd[1420]: Accepted password for custserv from 203.0.113.12 port 50213 ssh2\n" \
"2025-10-06T08:45:19Z server2 systemd-logind[410]: New session 16 of user custserv.\n" \
"2025-10-06T08:47:01Z server2 sudo:     custserv : TTY=pts/1 ; PWD=/home/custserv ; USER=root ; COMMAND=/usr/bin/tail -n 50 /var/log/app/tickets.log\n" \
"2025-10-06T08:47:02Z server2 app[2012]: [INFO] 2025-10-06T08:47:02Z - Retrieved 12 new customer tickets for processing\n"

audit_sysadmin = "\n2025-10-06T09:00:00Z server3 kernel: [    0.000000] Booting Linux on physical CPU 0x1\n" \
"2025-10-06T09:00:01Z server3 systemd[1]: Started Journal Service.\n" \
"2025-10-06T09:00:03Z server3 NetworkManager[812]: <info>  [2025-10-06T09:00:03Z] device (eth0): state change: unmanaged -> unavailable (reason 'managed')\n" \
"2025-10-06T09:00:06Z server3 sshd[1205]: Server listening on 0.0.0.0 port 22.\n" \
"2025-10-06T09:00:07Z server3 sshd[1205]: Server listening on :: port 22.\n" \
"2025-10-06T09:02:34Z server3 sshd[1350]: Accepted publickey for sysadmin from 198.51.100.55 port 61420 ssh2: RSA SHA256:Syst3mK3y...\n" \
"2025-10-06T09:02:35Z server3 systemd-logind[410]: New session 17 of user sysadmin.\n" \
"2025-10-06T09:04:12Z server3 sudo:     sysadmin : TTY=pts/2 ; PWD=/home/sysadmin ; USER=root ; COMMAND=/usr/bin/systemctl restart nginx\n" \
"2025-10-06T09:04:13Z server3 systemd[1]: Restarted nginx web server.\n"

#Roles
def user():
  if not mfa():
    print("Access denided: MFA not confirmed")
    return
  
  print("Type 'view' to view your account?\n" \
  "'transfer' to transfer money\n" \
  "'quit' to leave\n")
  while True:
   response = input()
   if response == "view":
     print("\nyour account balance:\n $5000\n")
     break
   elif response == "transfer":
    print("Who would you like to send money to?\n") \
  
   elif response == "quit":
    print("\nHave a good day!\n")
    sys.exit()
   else:
    print("only 'view', 'transfer' and 'quit' are acceptable")
    break
   while True:
     response = input()
     if response == "Bob":
       print("\nsending funds to Bob\n")
       return
     elif response == "Alice":
       print("\nsending funds to Alice\n")
       return
     elif response == "Xi":
       print("\nsending funds to Xi\n")
       return
     elif response == "Marcus":
       print("\nsending funds to Marcus\n")
       return
     else:
       response not in ("Bob", "Alice", "Xi", "Marcus")
       print("\nEnter a vaild name\n")

def CS():
  print("Enter the name of the customer to view their account:\n" \
  "\nBob\n" \
    "Alice\n" \
    "Xi\n" \
    "Marcus\n")
  response = input()
  while True:
   if response == "Bob":
     print(Bob)
     return
   elif response == "Alice":
     print(Alice)
     return
   elif response == "Xi":
     print(Xi)
     return
   elif response == "Marcus":
     print(Marcus)
     return
   elif response == "exit":
     print("\nGoodbye!")
     sys.exit()
  
   

def admin():
  print("What would you like to do?\n" \
  "\nview logs?\n" \
  "update accounts?\n" \
  "manage system?\n" \
  "exit")
  response = input()
  while True:
   if response == "view logs":
      print(audit)
      return
   elif response == "update system config":
      print("\naccounts updating.....\n")
      return
   elif response == "manage system":
      print("\naccess denied, must be senior admin\n")
      return
   elif response == "exit":
    print("\nHave a good day!\n")
    sys.exit()
   elif response not in ("view logs", "update accounts", "manage system", "exit"):
      print("only 'view logs', 'update accounts', 'manage system' and 'exit' are acceptable\n")
      return
   

def auditor():
  print("What would you like to view?\n" \
  "\nUser logs?\n" \
  "CS logs?\n" \
  "Admin logs?\n" \
  "exit\n")
  response = input()
  while True:
    if response == "User logs":
      print("\nWhich User logs do you want to view?\n" \
      "Bob\n" \
      "Alice\n" \
      "Xi\n" \
      "Marcus\n")
      while True:
       response = input()
       if response == "Bob":
        print(audit_bob)
        return
       elif response == "Alice":
        print(audit_alice)
        return
       elif response == "Xi":
        print(audit_xi)
        return
       elif response == "Marcus":
        print(audit_marcus)
        return
       elif response == "Admin":
        print(audit_sysadmin)
        return
       elif response not in ("Bob", "Alice", "Xi", "Marcus", "Customer Service"):
        print("\nEnter a vaild account\n")
        
    elif response == "CS logs":
        print(audit_custserv)
        return
    elif response == "Admin logs":
        print(audit_sysadmin)
        return
    elif response == "exit":
        print("Logging out\n" \
        "Have a good day!")
        sys.exit()
    else:
      print("Enter valid command")
      return
#login sim   
def login():
  print("enter your password or type 'exit' to leave")
  response = input()
  while True:
   if response == "asdf1234":
    user()
   elif response == "hello":
    CS()
   elif response == "098765":
    admin()
   elif response == "zxcvb":
    auditor()
   elif response == "exit":
    print("Logging out.....")
    sys.exit()
   else:
    print("incorrect password")
    response = input()
    continue
   
#MFA sim  
def mfa():
  while True:
   send = random.randint(0,1) == 1
   if not send:
     print("MFA not received, try again? y/n")
     if input() == 'y':
       continue
     return False
   code = str(random.randint(1000,9999))
   print("MFA code sent: " + code + " Enter code to confirm:")
   if input() == code:
     return True
   print("Incorrect code. Try again? y/n")
   if input() != 'y':
     return True
  


print("Enter your role:\n" \
"\nUser\n" \
"Customer Service\n" \
"Administrator\n" \
"Auditor\n" \
"Exit")
response = input()
while True:
 if response == "User":
   user()
 elif response == "Customer Service":
   CS()
 elif response == "Administrator":
   admin()
 elif response == "Auditor":
   auditor()
 elif response == "Exit":
   print("Logging out.....")
   sys.exit()
 else:
   print("Not a valid role")
   response = input()
   continue



