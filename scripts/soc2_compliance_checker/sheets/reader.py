# Reads data from Google Sheets

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config.settings import SCOPE, SHEET_NAME

def authenticate_google(credentials_json_path):
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_json_path, SCOPE)
    client = gspread.authorize(creds)
    return client.open(SHEET_NAME)

def get_checklist_rows(sheet):
    values = sheet.get_all_values()
    headers = values[0]
    rows = values[1:]  # skip header

    try:
        cli_col_index = headers.index("Evidence Notes")
        compliant_col_index = headers.index("Compliant?")
        applies_to_me_index = headers.index("Applies to Me?")
    except ValueError as e:
        raise Exception(f"Required column missing: {e}")

    checklist = []
    for i, row in enumerate(rows, start=2):
        applies = row[applies_to_me_index] if len(row) > applies_to_me_index else ""
        cli_command = row[cli_col_index] if len(row) > cli_col_index else ""
        if applies.strip().lower().startswith("y") and cli_command and "<bucket-name>" not in cli_command:
            checklist.append({
                "row_number": i,
                "cli_command": cli_command,
                "compliant_col_index": compliant_col_index
            })

    return checklist
