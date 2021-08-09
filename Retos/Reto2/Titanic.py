import pandas as pd
data = pd.read_csv("titanic.csv")

print("Longitud del dataframe\n" + str(data.__len__()) + "\n")
print("Nombre de las columnas\n", data.columns.values, "\n")
print("Nombre de las filas\n", data.index)
print("Tipo de datos de columnas\n", str(data.dtypes) + "\n")
print("Primeras 10 filas\n", str(data[:10]) + "\n")
print("Últimas 10 filas\n", str(data[-10:]) + "\n")
print("Datos del pasajero identificador 148\n", str(data.loc[data.loc[:, 'PassengerId'] == 148]) + "\n")
# print(data.loc[148])
print("filas Pares \n", str(data.iloc[range(0, data.shape[0], 2)]), "\n")
print("Personas en primera clase \n", str(data[data["Pclass"] == 1]['Name'].sort_values()), "\n")
print("Sobrevivieron y murieron \n ", str(data['Survived'].value_counts()/data['Survived'].count() * 100), "\n")
print("sobrevivientes por clase \n", str(data.groupby('Pclass')['Survived'].value_counts(normalize=True)), "\n")
# Asi elimino los que no tienen edad
data.dropna(subset=["Age"])
print("Edad media de mujeres por clas \n", str(data.groupby(['Pclass', 'Sex'])['Age'].mean().unstack()['female']), "\n")
data['Young'] = data['Age'] < 18
print(data)
print(data.groupby(['Pclass', 'Young'])['Survived'].value_counts(normalize = True) * 100)
