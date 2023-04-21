'Para importar usamos import_extension_as_nombre'

import pandas as pd
import numpy as np

#Para importar un archivo csv usamos pd_.read_csv(Direccion del archivo) en caso tengamos un separardor especial'
#Usamos sep=";" es un ejemplo y si hay un problema utf=8 cambiamos usando encoding
#enconding="latin-1"

ventas = pd.read_csv("C:/Users/HP/Desktop/ProyectoPython/Ventas.csv",sep=";", encoding='latin-1')
print(ventas.head())
print(ventas.head(100))

'Para saber el numero de datos y el tipo usamo info'
print(ventas.info())

'Para saber de algun campo especifico de la base de datos usamo value_counts'
print(ventas.value_counts("Sucursal"))
print(ventas.value_counts("Vendedor"))

'Para la estadistica descriptiva usamos describe'
print(ventas.describe())

import seaborn as sns
import matplotlib.pyplot as plt

'Si queremos graficar un histograma primero debmos configuara con el comando sns.histplot'
sns.histplot(data=ventas, x= "Total cobrado")
plt.show()

'Para especificar la frecuencia usamos binwidth'
sns.histplot(data=ventas, x= "Total cobrado", binwidth=1000)
plt.show()

'Para cambiar el timpo de un dato usamos ventas["Cantidad vendida"] = ventas["Cantidad Vendida"].astype (int)'
'Para valores enteros = int'
'Para valores string = str'
'Para valores float = float'
'Para valores dictionary = dict'
'Para valores lista = list'
'Para valores boleanos = bool'
ventas["Fecha"] = ventas["Fecha"].astype ('datetime64[as]')



'Si queremos verificar si un valor es un valor en especifico usamos isin'
ventas["Sucursal"].isin(["Abasto"])

'Para valores que no estan incluidos usamos~'
~ventas["Sucursal"].isin(["Abasto"])


'Si queremos ver este filtro usado y ver los 30 primero valores que lo cumplen'
ventas[ventas["Sucursal"].isin(["Abasto"])].head(30)

'Si queremos ver solo los datos que sean objetos'
ventas.select_dtypes(object).head()

'Si queremos ver solo los datos que sean numeros'
ventas.select_dtypes("number").head()

'Si queremos ver los min o maximos usamos min and max'
ventas["Total cobrado"].min()
ventas["Total cobrado"].max()

'Para hacer un grafico de cajas'
sns.boxplot(data=ventas, x= "Total cobrado")
plt.show()

'Si queremos agregar una variable solo usamos,'
sns.boxplot(data=ventas, x= "Total cobrado", y="Producto")
plt.show()

#Si queremos agrupar por usamos el comando grouby
#print[ventas.groupby("Total cobrado").mean()]

'Si queremos agregar solicitud de media o desvstan por usamos el comando agg'
ventas.agg(["mean", "std"])

'Si queremos elegir de que columna solicitar de media o desvstan por usamos el comando agg'
ventas.agg({"Total cobrado": ["mean", "std"], "Precio unitario": ["median"]})

#Add

'Si queremos agrupar por sucursal y elegir de que columna solicitar de media o desvstan por usamos el comando agg'
ventas.groupby("Sucursal").agg(mean_Total=("Total cobrado", "mean"), std_precio=("Precio unitario", "std"))


sns.barplot(data=ventas, x="Sucursal", y="Total cobrado") 
plt.show()


year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972] 
plt.plot(year, pop)
plt.show()


