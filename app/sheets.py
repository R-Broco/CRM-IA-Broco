import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_to_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("CRM-Psicologia").sheet1
    return sheet

def add_client(name, phone):
    sheet = connect_to_sheet()
    sheet.append_row([name, phone])
