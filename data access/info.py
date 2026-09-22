
# from this we can check :
# 1- number of rows and coloum
# 2- no null count
# 3- dtype
# 4- memory use

import pandas as pd

Data = {
    "Name":["Ankit","Suraj","Priyanshu"],
    "Age":[20,21,19],
    'Branch':["AI","CSE","ECE"],
    "Yr":[24,24,24]

}
df = pd.DataFrame(Data)
print(df)
print(df.info())