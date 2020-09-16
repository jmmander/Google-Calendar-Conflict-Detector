noAccounts = input("How many google accounts would you like to be monitored? ")
imessage = input("Would you like an iMessage notication? (y/n) ")
if imessage.lower() == "y" or imessage.lower() == "yes":
    phoneno = input("What phone number is associated with your iMessage account? Please include the + sign followed by your country code ")
else:
    phoneno = ""
notification = input("Would you like a notification on your Mac? (y/n) ")
path = input("What is the full path for the folder that holds cal.py? ")

text = "noAccounts =" + noAccounts + "\niMessage =" + imessage + "\nNotification =" + notification + "\nphoneno =" + phoneno + "\npath =" + path
f = open("setup.txt", "w")
f.write(text)
f.close()

