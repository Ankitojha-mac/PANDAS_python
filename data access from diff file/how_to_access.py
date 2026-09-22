import pandas as pd
df = pd.read_csv("sales_data_sample.csv",encoding="latin1") 


# (use latin1 and utf-8 when error is showing)


df1 = pd.read_json("sample_Data.json",encoding="latin1")
df2 = pd.read_excel("SampleSuperstore.xlsx")
print(df)
print(df1)
print(df2)
