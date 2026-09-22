import pandas as pd

Data = {
    "Name":["Ankit","Suraj","Priyanshu"],
    "Age":[20,21,19],
    'Branch':["AI","CSE","ECE"],
    "Yr":[24,24,24]

}
df = pd.DataFrame(Data)
print(df)

# ROW wise access
# head for starting first
# tail for ending first
print(df.head(1))
print(df.tail(1))
