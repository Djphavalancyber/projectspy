import pandas as pd 
df = pd.read_csv("AssetHistoryDelta_99514666 (1).csv")
pd.set_option("display.max_columns",None)
print(df.shape)
print(df.head())
print(df.columns.tolist())
print(df.dtypes)
print(df["Date"].head())

df["Date"]=pd.to_datetime(df["Date"])
df["hour"]=df["Date"].dt.hour
print(df["hour"].value_counts.sortcome ☆*: .｡. o(≧▽≦)o .｡.:*☆. oh