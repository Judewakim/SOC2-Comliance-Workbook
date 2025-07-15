# Orchestrates which check to run

from sheets.reader import get_checklist_rows
from sheets.writer import update_compliance_result
from utils.aws_cli import run_aws_cli
# from compliance.logic import evaluate_compliance
from time import sleep

def run_compliance_check(sheet):
    try:
        rows = get_checklist_rows(sheet)
    except Exception as e:
        print(e)
        return

    for idx, row in enumerate(rows, start=1):
        print(f"Running check {idx} of {len(rows)}")
        result = run_aws_cli(row["cli_command"])
        status = evaluate_compliance(result)
        update_compliance_result(sheet, row["row_number"], row["compliant_col_index"], status)
        sleep(0.5)
