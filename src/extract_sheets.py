import pandas as pd

# Extract average values from a given data frame
def get_date_list(file):
    # Load the Excel file
    excel_file = pd.ExcelFile('Monthly FTSE Data - New.xlsx')

    # Get the list of sheet names
    sheet_names = []
    
    for sheet in excel_file.sheet_names:
        if not sheet.endswith("Opt") and sheet[0].isdigit():
            sheet_names.append(sheet)

    # Print the list of sheet names
    return sheet_names