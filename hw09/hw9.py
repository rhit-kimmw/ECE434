#!/usr/bin/env python3
# Based pm: https://github.com/googleworkspace/python-samples/tree/master/sheets/quickstart
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START sheets_quickstart]
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time, sys
import time

# get path for temperature sensors(one wire)
path = "/sys/class/hwmon/hwmon"
sens0 = path + "0/temp1_input"
sens1 = path + "1/temp1_input"
sens2 = path + "2/temp1_input"
temp0 = open(sens0, 'r')
temp1 = open(sens1, 'r')
temp2 = open(sens2, 'r')

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Qq1abWOPXPoykrmv8y4Qghy7lYY3xB-V6oDtFKgl6qg'
SAMPLE_RANGE_NAME = 'A2'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            # creds = flow.run_local_server(port=0)
            creds = flow.run_console()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    
    count = 0
    while count < 100:
        temp0.seek(0)
        temp1.seek(0)
        temp2.seek(0)
        try:
            T0 = float(temp0.read()[:-1])/1000.0
            T1 = float(temp1.read()[:-1])/1000.0
            T2 = float(temp2.read()[:-1])/1000.0
            
            print("T0:",T0,"T1:",T1,"T2:",T2)
        except KeyboardInterrupt:
            exit()
        except:
            print("error")
            continue 
        sheet = service.spreadsheets()
        values = [ [time.time()/60/60/24+ 25569 - 5/24, T0, T1, T2]]
        body = {'values': values}
        result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME,
                                    valueInputOption='USER_ENTERED', 
                                    body=body
                                    ).execute()
        count += 1
        print(result)

if __name__ == '__main__':
    main()
# [END sheets_quickstart]
