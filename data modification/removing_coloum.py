import pandas as pd
Data = {
    "Name":["Ankit","Priyanshu","Suraj"],
    "Branch":["AIML","ECE","CSE"],
    "Pay_method":["Cash","DRCC","DRCC"],
    "Fee":["Not paid","Paid","Paid"],
    "Bus":["No","Yes","Yes"],
    "Attendence":[73,59,90],
    "Mid_sem_left":[12,4,12],
}
df=pd.DataFrame(Data)
print(df)
print("")
print("After removing column")
#to delete certain column
df.drop(columns=["Mid_sem_left"], inplace=True)
print(df)

