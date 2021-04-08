from googleapiclient.discovery import build
from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1PNnLQQVzg0WAWZkXBJskFmpbjGiu9iEeyO3jqUVWk38'




service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Powerful people!A1:E51").execute()
values = result.get('values', [])

aoa=[["#51","Michael Bloomberg","Bloomberg","79","Entrepreneur"],["#52","Wang Jianlin","Dalian Wanda Group","66","Entrepreneur"]]

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet2!A2", valueInputOption="USER_ENTERED", body={"values":aoa}).execute()


print(request)

