import pandas as pd


income = pd.read_csv('bill_data\\income.csv')
income['日期'] = pd.to_datetime(income['日期'],format='%Y%m%d')
income['日期'] = income['日期'].dt.strftime('%Y-%m-%d')
income.to_csv('bill_data\\income.csv', index=False, encoding="utf-8-sig")

expenditure = pd.read_csv('bill_data\\expenditure.csv')
expenditure['日期'] = pd.to_datetime(expenditure['日期'],format='%Y%m%d')
expenditure['日期'] = expenditure['日期'].dt.strftime('%Y-%m-%d')
expenditure.to_csv('bill_data\\expenditure.csv', index=False, encoding="utf-8-sig")

balance = pd.read_csv('bill_data\\balance.csv')
balance['日期'] = pd.to_datetime(balance['日期'],format='%Y%m%d')
balance['日期'] = balance['日期'].dt.strftime('%Y-%m-%d')
balance.to_csv('bill_data\\balance.csv', index=False, encoding="utf-8-sig")