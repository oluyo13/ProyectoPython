'Para importar usamos import_extension_as_nombre'

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Para importar un archivo csv usamos pd_.read_csv(Direccion del archivo) en caso tengamos un separardor especial'
#Usamos sep=";" es un ejemplo y si hay un problema utf=8 cambiamos usando encoding
#enconding="latin-1"

sales = pd.read_csv("C:/Users/HP/Desktop/ProyectoPython/sales_data.csv",sep=",", encoding='latin-1')
sales.head()

'Para saber el numero de datos y el tipo usamo info'
print(sales.info())
#Una forma reducida es usando shape
sales.shape

'To know the stats descriptives we use describe()'
sales.describe( )

#To know the s.d of the just one colunm
sales["Unit_Cost"].describe()

'Si solo queremos una estadistica'
sales["Unit_Cost"].mean()

#Algunas graficas son:
sales["Unit_Cost"].plot(kind='box', vert=False, figsize=(14,6))
plt.show()

sales.plot(kind ='scatter',x='Revenue',y='Profit')
plt.show()

sales['Unit_Cost'].plot(kind ='density',figsize=(14,6))
plt.show()

'Histograma'
ax =sales['Unit_Cost'].plot(kind ='hist',figsize=(14,6))
ax.set_ylabel("Numero de ventas")
ax.set_xlabel("Dolares")
plt.show()

#Para contar los valores dentro de una columna usammos counts
sales['Age_Group'].value_counts()
'Si apartir de eso queremos hacer un grafico de pastel'
pie=sales['Age_Group'].value_counts().plot(kind='pie',figsize=(14,6))
pie.set_ylabel("Porcentaje")
plt.show()


#Si queremos hacer un analisis de correlacion usamos el comando corr()
sales.corr()

#Si queremos crear una nueva columna
sales['Revenue_per_age']=sales['Revenue']/sales['Customer_Age']
sales['Revenue_per_age'].head()

sales['Calculated_Cost']=sales['Order_Quantity']*sales['Unit_Cost']
sales['Calculated_Cost'].head()


#Para exportar un dataframe a csv o excel
sales.to_csv('New Sales.csv')
sales.to_excel('New Sales.csv')
sales.to_csv('New Sales.csv', index=False)
sales.to_csv('New Sales.csv', index=False, sep=';')