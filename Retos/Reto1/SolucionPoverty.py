import numpy as np
import pandas as pd
df=pd.read_csv("Poverty.csv")

mins=df.min()
maxi=df.max()

print("Min of each column:")
print(mins)

print("Max of each Columns")
print(maxi)