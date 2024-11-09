import pandas as pd


def standard_usd(curr):
    if curr == 'Dollars' or curr == '$$':
        return 'USD'
    return curr


df = pd.read_excel('movies_db.xlsx', 'financials', converters={
    'currency': standard_usd
})

print(df)

