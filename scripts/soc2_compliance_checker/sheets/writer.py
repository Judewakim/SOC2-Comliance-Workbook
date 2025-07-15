# Writes results to Google Sheets
#COME BACK TO THIS

def update_compliance_result(sheet, row_number, col_index, result):
    sheet.update_cell(row_number, col_index + 1, result)
