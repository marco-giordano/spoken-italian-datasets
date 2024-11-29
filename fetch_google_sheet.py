import os
import json
from oauth2client.service_account import ServiceAccountCredentials

# Load the service account JSON from the GitHub secret
SERVICE_ACCOUNT_INFO = json.loads(os.environ["SERVICE_ACCOUNT_JSON"])

# Google Sheets API setup
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SPREADSHEET_ID = "18S66CG2-pX25rzP91b1Fc6KIOTfovfiKXrF_ggybMBA"  # Replace with your Google Sheet ID
SHEET_NAME = "GitHubRepo"  # Replace with your sheet's name

def fetch_google_sheet():
    # Authenticate using the service account credentials
    creds = ServiceAccountCredentials.from_json_keyfile_dict(SERVICE_ACCOUNT_INFO, SCOPES)
    client = gspread.authorize(creds)

    # Access the Google Sheet and fetch the data
    sheet = client.open_by_key(SPREADSHEET_ID)
    worksheet = sheet.worksheet(SHEET_NAME)
    data = worksheet.get_all_records()

    # Convert to a pandas DataFrame
    df = pd.DataFrame(data)

    # Save the data locally as a CSV file
    output_file = "data/spoken_italian_datasets.csv"
    os.makedirs("data", exist_ok=True)  # Ensure the directory exists
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    fetch_google_sheet()
