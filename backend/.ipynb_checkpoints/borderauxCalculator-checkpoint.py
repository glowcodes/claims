import pandas as pd

premium_ws=pd.read_excel(
    "bordereaux.xlsx", 
    engine='openpyxl', 
    sheet_name='Premium Bordereaux'
    )

claims_ws=pd.read_excel(
    "bordereaux.xlsx", 
    engine='openpyxl', 
    sheet_name='Claims Bordereaux'
    )

#premium_ws.columns=premium_ws.columns.str.lower().str.strip()
#claims_ws.columns=claims_ws.columns.str.lower().str.strip()

print(premium_ws.head())