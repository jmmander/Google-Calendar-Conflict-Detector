from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import subprocess
import os
import time



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
path = os.path.dirname(os.path.abspath(__file__))


def setup():

    if os.path.isfile('./myconfig.txt'):
        f = open("myconfig.txt", "r")
        config = f.readlines()
        f.close()
        if len(config) == 4:
            print("checking myconfig.txt")
            setupdic = {}
            for line in config:
                comps = line.split("=")
                varname = comps[0]
                val = comps[1].strip('\n')
                setupdic[varname] = val
        else:
            setupdic = questionAsker()
    else:
        setupdic = questionAsker()

    return setupdic


def questionAsker():
    inputdic = {}
    noAccounts = raw_input("How many google accounts would you like to be monitored? ")
    imessage = raw_input("Would you like an iMessage notication? (y/n) ")
    if imessage.lower() == "y" or imessage.lower() == "yes":
        phoneno = raw_input("What phone number is associated with your iMessage account? Please include the + sign followed by your country code ")
    else:
        phoneno = ""
    notification = raw_input("Would you like a notification on your Mac? (y/n) ")
    text = "noAccounts=" + noAccounts + "\nimessage=" + imessage + "\nnotification=" + notification + "\nphoneno=" + phoneno + "\n"
    f = open("myconfig.txt", "w")
    f.write(text)
    print("wrote to myconfig.txt")
    f.close()

    inputdic["noAccounts"] = noAccounts
    inputdic["imessage"] = imessage
    inputdic["phoneno"] = phoneno
    inputdic["notification"] = notification

    return inputdic



def getEvents(path):

    # Call the Calendar API
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(path):
        with open(path, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(path, 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)


    #now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    tomorrow = tomorrow.replace(hour=0, minute=0, second=0)
    days_after = tomorrow + datetime.timedelta(days=7)
    iso_start = tomorrow.isoformat() + "Z"
    iso_end = days_after.isoformat() + "Z"


    events_result = service.events().list(calendarId='primary', timeMin=iso_start,
                                        timeMax=iso_end, singleEvents=True,
                                        orderBy='startTime').execute()

    events = events_result.get('items', [])

    return events

def iso_to_datetime(iso):
    iso_split = iso.split("T")
    iso_date = iso_split[0]
    date_split = iso_date.split("-")
    print(date_split)
    iso_time = iso_split[1]
    time_split = iso_time.split(":")[:2]
    print(time_split)
    date_time_obj = datetime.datetime(int(date_split[0]), int(date_split[1]), int(date_split[2]), int(time_split[0]), int(time_split[1], 0))

    return date_time_obj

def check_for_conflicts(events):
    all = []
    if not events:
        print('No upcoming events found.')
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            name = event['summary']
            end = event['end'].get('dateTime', event['end'].get('date'))
            tup = (name, (start, end))
            all.append(tup)
            print(tup)
        conflicts = ["Conflicts: \n\n", ]
        i=0
        if "+" in all[0][1][1]:
            time_diff = all[0][1][1].split("+")[1]
            time_diff_hours = 24 - int(time_diff.split(":")[0])
            time_diff_min = int(time_diff.split(":")[1])
            time_diff_delta = datetime.timedelta(hours=time_diff_hours, minutes=time_diff_min)
        else:
            time_diff_delta = datetime.timedelta(hours=0)
        for element in all:
            start = iso_to_datetime(element[1][0]) - time_diff_delta
            end = iso_to_datetime(element[1][1]) - time_diff_delta
            name = element[0]
            i=i+1
            for other_event in all[i:]:
                other_start = iso_to_datetime(other_event[1][0]) - time_diff_delta
                other_end = iso_to_datetime(other_event[1][1]) - time_diff_delta
                other_name = other_event[0]
                if start.date() == other_start.date() and end.date() == other_end.date():
                    overlap = max(start.time(), other_start.time()) < min(end.time(), other_end.time())
                    if overlap:
                        date_str = start.strftime("%m/%d")
                        line = date_str + ": " + name + " and " + other_name + " share a conflict\n"
                        conflicts.append(line)
        return conflicts


def sendMessage(conflicts, phoneno):
    ##send imessage

    msg = "".join(conflicts)
    scpt = "sendMessage.scpt"
    args = [phoneno, msg]

    p = subprocess.Popen(
       ['/usr/bin/osascript', scpt] + [str(arg) for arg in args],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = p.communicate()

    if p.returncode:
        print('ERROR:', stderr)
    else:
        print(stdout)


def createNotication(conflicts):
    ##create notification

    script = "notification.scpt"

    p = subprocess.Popen(
        ['/usr/bin/osascript', script],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = p.communicate()

    if p.returncode:
        print('ERROR:', stderr)
    else:
        print(stdout)



def createCron(path):
    ##create cronjob
    p = subprocess.Popen(
        ['sh', 'schedule.sh', path],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = p.communicate()

    if p.returncode:
        print('ERROR:', stderr)
    else:
        print(stdout)


eventlist = []
setupdic = setup()

for num in range(int(setupdic["noAccounts"])):
    tokenno = "token" + str(num) + ".pickle"
    events = getEvents(tokenno)
    if events:
        eventlist.append(events)
print("\n\nChecking tomorrows events...\n")
if len(eventlist) > 0:
    all_events = [item for sublist in eventlist for item in sublist]
else:
    all_events = None
if all_events:
    conflicts = check_for_conflicts(all_events)
    if len(conflicts) > 1:
        print("Uh oh! Conflicts found!")
        if setupdic["imessage"].lower() == "y" or setupdic["imessage"].lower() == "yes":
            print("Sending iMessage...")
            sendMessage(conflicts, setupdic["phoneno"])
        if setupdic["notification"].lower() == "y" or setupdic["notification"].lower() == "yes":
            print("Creating notification...")
            createNotication(conflicts)
    time.sleep(6)
    print("Creating cronjob...")
    createCron(path)
    print("\n\nAll done! Your conflict detector has been set up and will now automatically run every hour. You will only be notified if you have a conflict! \n\n")
else:
    print("No conflicts tomorrow")
    print("Creating cronjob...")
    createCron(path)
    print("\n\nAll done! Your conflict detector has been set up and will now automatically run every hour. You will only be notified if you have a conflict! \n\n")


