import pandas as pd

Data = {
    "Name":["Ankit","Suraj","Priyanshu"],
    "Age" : [20,21,19],
    "Place" : ["Ara" , "Gopalganj", "Siwan"]
}

df = pd.DataFrame(Data)
print(df)

# df.to_csv is use to convert into csv file

df.to_csv("output.csv",index = False)

# df.to_csv is use to convert into csv file

df.to_excel("output.xlsx",index = False)

# df.to_csv is use to convert into csv file

df.to_json("output.json",index = False)