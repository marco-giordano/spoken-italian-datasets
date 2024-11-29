import os
import json
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


SERVICE_ACCOUNT_INFO = json.loads(os.environ["SERVICE_ACCOUNT_JSON"])


SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SPREADSHEET_ID = "18S66CG2-pX25rzP91b1Fc6KIOTfovfiKXrF_ggybMBA"  # Replace with your Google Sheet ID
SHEET_NAME = "GitHubRepo"

def fetch_google_sheet():
    
    creds = ServiceAccountCredentials.from_json_keyfile_dict(SERVICE_ACCOUNT_INFO, SCOPES)
    client = gspread.authorize(creds)

    
    sheet = client.open_by_key(SPREADSHEET_ID)
    worksheet = sheet.worksheet(SHEET_NAME)
    data = worksheet.get_all_records()

    
    df = pd.DataFrame(data)

    
    output_file = "data/spoken_italian_datasets.csv"
    os.makedirs("data", exist_ok=True)  # Ensure the directory exists
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    fetch_google_sheet()
