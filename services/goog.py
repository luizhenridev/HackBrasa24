from __future__ import print_function
import pandas as pd

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
#LUIZ
SAMPLE_SPREADSHEET_ID = '1pSaeUKxJdFgw4D9t0EzYBRBCC6rSXswgvE2qqovw7U4'
SAMPLE_RANGE_NAME = 'teste2!C:H'
#PAULO
SAMPLE_SPREADSHEET_IDP = '1PjOmfOKuU1ORlWmTO7LfvU_Lmd5HAYTDHrO_ULrc3iM'
SAMPLE_RANGE_NAMEP = 'TABELA!C:Q'
#ANDREY
SAMPLE_SPREADSHEET_IDA = 'fEfzNNr2Q8jp5N3mhC4-z5W9SsJeGqU6mBc0gKw8Q_M'
SAMPLE_RANGE_NAMEA = 'TABELA!C:Q'
#VICTOR
SAMPLE_SPREADSHEET_IDV = '17XHk3v2YJcSS9eon8wyWnltEt2NXGHAn-jPXRBSJhDA' 
SAMPLE_RANGE_NAMEV = 'TABELA!C:Q'
#JOAO
SAMPLE_SPREADSHEET_IDJ = '1i9azehdO7NDUjhv9WHYmvmDCSbHy-ECkHIi9unse798'
SAMPLE_RANGE_NAMEJ = 'TABELA!C:Q'
#GABRIEL
SAMPLE_SPREADSHEET_IDG = '1YB6GNy7qEovTYfkS9-tUWMVlxTR47eN2spWR5zXfIIg'
SAMPLE_RANGE_NAMEG = 'TABELA!C:Q'
#CARLOS FILHO
SAMPLE_SPREADSHEET_IDCF = '1lgVCB4SqvXXW8wZmc1OUwsLDXxQhUS-QMovq5Eph89U'
SAMPLE_RANGE_NAMECF = 'TABELA!C:Q'
#MATHEUS
SAMPLE_SPREADSHEET_IDM = '1XL3kpfksPYxFBqFDVKbM9JTZg_BBKheFqzzECp3_06U'
SAMPLE_RANGE_NAMEM = 'TABELA!C:Q'


#SAMPLE_RANGE_NAME2 = 'Despesa Fixa!C:Q'
#SAMPLE_RANGE_NAME2 = 'Open5!A:F'



def main(userId):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        if userId == 2022078829:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=SAMPLE_RANGE_NAME).execute()
            values = result.get('values', [])
            print(values)
            return values
        
        elif userId == 1081219056:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_IDP,
                                        range=SAMPLE_RANGE_NAMEP).execute()
            values = result.get('values', [])
            print(values)
            return values
        
        elif userId == 1088540336:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_IDA,
                                        range=SAMPLE_RANGE_NAMEA).execute()
            values = result.get('values', [])
            print(values)
            return values
        
        elif userId == 20:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_IDV,
                                        range=SAMPLE_RANGE_NAMEV).execute()
            values = result.get('values', [])
            print(values)
            return values
        
        elif userId == 30:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_IDJ,
                                        range=SAMPLE_RANGE_NAMEJ).execute()
            values = result.get('values', [])
            print(values)
            return values
        
        elif userId == 40:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_IDCF,
                                        range=SAMPLE_RANGE_NAMECF).execute()
            values = result.get('values', [])
            print(values)
            return values
        
        elif userId == 50:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_IDM,
                                        range=SAMPLE_RANGE_NAMEM).execute()
            values = result.get('values', [])
            print(values)
            return values
        
        else:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_IDG,
                                        range=SAMPLE_RANGE_NAMEG).execute()
            values = result.get('values', [])
            print(values)
            return values
        

        
        
    except HttpError as err:
        print(err)

def filtro(categoria):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        df = pd.DataFrame(values[1:], columns=values[0])

        dados_filtrados = (df[df['Segmentação'] == categoria ])
 

        n = 200
        
        list_df = [dados_filtrados[i:i+n] for i in range(0,len(dados_filtrados),n)]
        

        for i in list_df:
            print(i)
            print(len(list_df))
            return i
        
       
        
        


        
    except HttpError as err:
        print(err)


def input(lista):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        valor_adicionar = lista
        result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME,valueInputOption="USER_ENTERED", body={'values': valor_adicionar}).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()