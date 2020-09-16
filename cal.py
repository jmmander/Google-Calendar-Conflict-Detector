from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import subprocess

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


phoneno = "+13058505472"
path = "/Users/Jacqueline/PycharmProjects/calendar"

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
    day_after = tomorrow + datetime.timedelta(days=1)
    iso_start = tomorrow.isoformat() + "Z"
    iso_end = day_after.isoformat() + "Z"


    events_result = service.events().list(calendarId='primary', timeMin=iso_start,
                                        timeMax=iso_end, singleEvents=True,
                                        orderBy='startTime').execute()

    events = events_result.get('items', [])

    return events


def checkForConflicts(events):
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

        conflicts = ["Conflicts for tomorrow: \n\n", ]
        i=0
        for element in all:
            start_time = element[1][0]
            end_time = element[1][1]
            name = element[0]
            i=i+1
            for other_event in all[i:]:
                other_start = other_event[1][0]
                other_end = other_event[1][1]
                other_name = other_event[0]
                if end_time <= other_start and start_time <= other_end:
                    pass
                else:
                    if start_time <= other_start and end_time >= other_end:
                        conflict = (other_start,other_end)
                    elif start_time <= other_start and end_time <= other_end:
                        conflict = (other_start, end_time)
                    elif start_time >= other_start and end_time >= other_end:
                        conflict = (start_time, other_end)
                    else:
                        conflict = (start_time, end_time)
                    line = name + " and " + other_name + " share a conflict\n"

                    conflicts.append(line)
        return conflicts


def sendMessage(conflicts):
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



def createCron():
    ##create cronjob
    p = subprocess.Popen(
        ['sh', 'schedule.sh'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = p.communicate()

    if p.returncode:
        print('ERROR:', stderr)
    else:
        print(stdout)


events1 = getEvents('token.pickle')
events2 = getEvents('token1.pickle')
events = events1 + events2
if events:
    conflicts = checkForConflicts(events)
    if len(conflicts) > 1:
        sendMessage(conflicts)
        createNotication(conflicts)
        createCron()
else:
    print("No conflicts tomorrow")


