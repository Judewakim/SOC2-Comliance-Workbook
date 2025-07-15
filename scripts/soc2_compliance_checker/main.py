# Entry point for running the whole process

from config.settings import CREDENTIALS_JSON_PATH
from sheets.reader import authenticate_google, get_checklist_rows
from compliance.runner import run_compliance_check

def run_all_checks():
    print("Authenticating to Google Sheets...")
    workbook = authenticate_google(CREDENTIALS_JSON_PATH)
    sheet_titles = [s.title for s in workbook.worksheets()]

    for title in sheet_titles:
        if title.lower() == "executive summary":
            continue
        print(f"Processing sheet: {title}")
        sheet = workbook.worksheet(title)
        run_compliance_check(sheet)

    print("Compliance checks complete.")

if __name__ == "__main__":
    run_all_checks()
