import boto3
import gspread
import subprocess
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep

# Define Google Sheets access
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
SHEET_NAME = "Amaani SOC2 Compliance Workbook"

def authenticate_google(credentials_json_path):
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_json_path, SCOPE)
    client = gspread.authorize(creds)
    return client.open(SHEET_NAME)

def run_aws_cli(command):
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return result.strip()
    except subprocess.CalledProcessError:
        return None

def evaluate_compliance(result):
    if result:
        return "✅"
    else:
        return "❌"

def process_sheet(sheet):
    values = sheet.get_all_values()
    headers = values[0]
    rows = values[1:]  # Skip header

    try:
        cli_col_index = headers.index("Evidence Notes")
        compliant_col_index = headers.index("Compliant?")
        applies_to_me_index = headers.index("Applies to Me?")
    except ValueError as e:
        print(f"Required column missing: {e}")
        return

    # Filter rows that apply and have a CLI command
    checklist_rows = []
    for i, row in enumerate(rows, start=2):
        applies = row[applies_to_me_index] if len(row) > applies_to_me_index else ""
        cli_command = row[cli_col_index] if len(row) > cli_col_index else ""
        if applies.strip().lower().startswith("y") and cli_command and "<bucket-name>" not in cli_command:
            checklist_rows.append((i, cli_command))

    total_checks = len(checklist_rows)

    for idx, (row_number, cli_command) in enumerate(checklist_rows, start=1):
        print(f"Running check {idx} of {total_checks}")
        result = run_aws_cli(cli_command)
        status = evaluate_compliance(result)
        sheet.update_cell(row_number, compliant_col_index + 1, status)
        sleep(0.5)



def run_all_checks(credentials_json_path):
    print("Authenticating to Google Sheets...")
    workbook = authenticate_google(credentials_json_path)
    sheet_titles = [s.title for s in workbook.worksheets()]
    for title in sheet_titles:
        if title.lower() == "executive summary":
            continue
        print(f"Processing sheet: {title}")
        sheet = workbook.worksheet(title)
        process_sheet(sheet)
    print("Compliance checks complete.")

if __name__ == "__main__":
    run_all_checks("credentials.json")
