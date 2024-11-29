import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API setup
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SERVICE_ACCOUNT_FILE = "path/to/your/service-account.json"  # Update with your file path
SPREADSHEET_ID = "18S66CG2-pX25rzP91b1Fc6KIOTfovfiKXrF_ggybMBA"  # Replace with your Google Sheet ID
SHEET_NAME = "GitHubRepo"  # Replace with the name of the sheet you want to clone

def fetch_google_sheet():
    # Authenticate with Google Sheets API
    creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)
    client = gspread.authorize(creds)

    # Open the Google Sheet and get the data
    sheet = client.open_by_key(SPREADSHEET_ID)
    worksheet = sheet.worksheet(SHEET_NAME)
    data = worksheet.get_all_records()

    # Convert to a pandas DataFrame
    df = pd.DataFrame(data)

    # Save as a CSV file in the repository
    output_file = "data/spoken_italian_datasets.csv"
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    fetch_google_sheet()
