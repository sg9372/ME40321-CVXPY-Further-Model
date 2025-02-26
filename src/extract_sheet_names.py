import pandas as pd

# Extract average values from a given data frame
def get_sheet_names(file):
    # Load the Excel file
    excel_file = pd.ExcelFile('Monthly FTSE Data - New.xlsx')

    # Get the list of sheet names
    sheet_names = []
    
    for sheet in excel_file.sheet_names:
        if not sheet.endswith("Opt") and not sheet.endswith("opt") and sheet[0].isdigit():
            sheet_names.append(sheet)
    
    # Sort the sheet names in chronological order
    sheet_names.sort(key=lambda date: pd.to_datetime(f"01_{date}" if len(date.split('_')) < 3 else date, format='%d_%m_%Y', errors='coerce'))
    
    # Make "01_2020" into "01_01_2020" and have sheet_names and dates seperate
    dates = []
    for i in range(len(sheet_names)):
        if len(sheet_names[i].split('_')) < 3:
            dates.append(f"01_{sheet_names[i]}")
        else:
            dates.append(sheet_names[i])

    # Print the list of sheet names
    return sheet_names, dates