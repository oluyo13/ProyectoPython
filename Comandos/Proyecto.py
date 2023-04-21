import numpy as np
import matplotlib.pyplot as plt


'Probando algunos graficos'
#Estos comandos en Python utilizan la biblioteca NumPy para crear un arreglo de datos "x" y una matriz de datos "y"
#np.linspace(0, 10, 500) genera un arreglo de 500 números 
# igualmente espaciados en el rango de 0 a 10. Estos números se almacenan en la variable x.

#np.random.randn(500, 6) genera una matriz de 500 filas y 6 columnas de números aleatorios 
# distribuidos normalmente (con media 0 y desviación estándar 1). Luego, np.cumsum() se aplica a lo largo del eje 0 (a lo largo de las filas) de esta matriz para obtener una matriz y que contiene la suma acumulativa de los números aleatorios generados en cada columna.

x = np.linspace(0, 10, 500)
y = np.cumsum(np.random.randn(500, 6), 0)

plt.figure(figsize=(12, 7))
plt.plot(x, y)

#Para crear una legenda, usamos ABCDEF es una cadena de texto que se utiliza 
# para etiquetar las líneas o puntos en el gráfico. En este caso, se etiquetará con las letras A, B, C, D, E y F
#ncol=2 especifica el numero de columnas 
#loc='upper left' especifica la posición de la leyenda en el gráfico. 
# En este caso, la leyenda se ubicará en la esquina superior izquierda del gráfico.
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()


import requests
import pandas as pd

def get_historic_price(symbol, exchange='bitfinex', after='2018-09-01'):
    url = 'https://api.cryptowat.ch/markets/{exchange}/{symbol}usd/ohlc'.format(
        symbol=symbol, exchange=exchange)
    resp = requests.get(url, params={
        'periods': '3600',
        'after': str(int(pd.Timestamp(after).timestamp()))
    })
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data['result']['3600'], columns=[
        'CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume', 'NA'
    ])
    df['CloseTime'] = pd.to_datetime(df['CloseTime'], unit='s')
    df.set_index('CloseTime', inplace=True)
    return df


last_week = (pd.Timestamp.now() - pd.offsets.Day(7))
last_week
btc = get_historic_price('btc', 'bitstamp', after=last_week)
eth = get_historic_price('eth', 'bitstamp', after=last_week)

btc.head()
btc['ClosePrice'].plot(figsize=(15, 7))

eth.head()
eth['ClosePrice'].plot(figsize=(15, 7))


import bokeh as bk

from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook

p1 = figure(x_axis_type="datetime", title="Crypto Prices", width=800)
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Price'

p1.line(btc.index, btc['ClosePrice'], color='#f2a900', legend='Bitcoin')
#p1.line(eth.index, eth['ClosePrice'], color='#A6CEE3', legend='Ether')

p1.legend.location = "top_left"

show(p1)


writer = pd.ExcelWriter('cryptos.xlsx')
#We'll now write both our Bitcoin and Ether data as separate sheets:

btc.to_excel(writer, sheet_name='Bitcoin')
eth.to_excel(writer, sheet_name='Ether')

# And finally, we can save the file:
writer.close()
