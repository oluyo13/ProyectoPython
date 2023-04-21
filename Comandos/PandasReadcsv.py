import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Leer csv
df = pd.read_csv('C:/Users/HP/Desktop/ProyectoPython/btcmarketprice.csv', header=None)
df.head()

#Si no hay header, definimos las columnas
df.columns = ['Timestamp', 'Price']
df.shape
df.head()

#Para ver los ultimos 3 registros
df.tail(3)

#Para saber el tipo de datos
df.dtypes

#Para ver el encabezado
pd.to_datetime(df['Timestamp']).head()
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.head()

#Si queremos un dato en especifico
df.set_index('Timestamp', inplace=True)
df.head()
df.loc['2017-09-29']

plt.show()
plt.plot(df.index, df['Price'])
x = np.arange(-10, 11)
plt.plot(x, x ** 2)