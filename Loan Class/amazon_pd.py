import pandas as pd

df = pd.read_csv('C:\\Users\\zwalk\\Documents\\Python Projects\\Loan Class\\amazon-orders.csv')
df = df.fillna(0)
df["Total Charged"] = df["Total Charged"].str.replace('$','').astype(float)

print(df)