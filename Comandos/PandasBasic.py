import pandas as pd
import numpy as np

# Para definir unas serie solo la creamos con pd.Series
# Esta series es de la poblacion de los 7 paises en millones
g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
g7_pop

#Para asignar un nombre usamos la funcion .name
g7_pop.name = 'Poblacion en millones G7'
g7_pop

#Podemos utilizar la posicion para pedir algun valor
g7_pop[0]
g7_pop[1]

#Podemos utilizar la funcion index para conocer como esta
g7_pop.index

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Para poder definir el indece, usamos .index=
g7_pop.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]
g7_pop

#Otra forma de hacer una series es de la siguiente manera
g8_pop=pd.Series({
    'Canada': 35.467,
    'France': 63.951,
    'Germany': 80.94,
    'Italy': 60.665,
    'Japan': 127.061,
    'United Kingdom': 64.511,
    'United States': 318.523
}, name='G8 Population in millions')
g8_pop

#Y la ultima forma es:
g9_index=pd.Series(
    [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
    index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom',
       'United States'],
    name='G9 Population in millions')
g9_index 

#Si queremos seleccionar algunos paises lo podemos hacer:
pd.Series(g7_pop, index=['France', 'Germany', 'Italy', 'Spain'])


g7_pop['Japan']

#Selecionar por la posicion
g7_pop.iloc[0]
g7_pop.iloc[-1]

#Seleccionar por pedido explicito
g7_pop[['Italy', 'France']]

#Boleanos (V/F)
g7_pop > 70

#Si queremos que nos muestre los valores
g7_pop[g7_pop > 70]
'Sacamos el promedio'
g7_pop.mean()
'Ahora si queremos sacar los valores mayores al promedio'
g7_pop[g7_pop > g7_pop.mean()]

#Podmeos poner la condicion que queramos
# ~ not
# | or
# & and
g7_pop[(g7_pop > g7_pop.mean() - g7_pop.std() / 2) | (g7_pop > g7_pop.mean() + g7_pop.std() / 2)]

#OPERACIONES
g7_pop * 1_000_000 

'En logaritmos'
np.log(g7_pop)

#Diferentes operaciones
g7_pop[(g7_pop > 80) | (g7_pop < 40)]
g7_pop[(g7_pop > 80) & (g7_pop < 200)]

#Modificando series
g7_pop['Canada'] = 40.5
g7_pop[g7_pop < 70]
g7_pop[g7_pop < 70] = 99.99

#Data: https://github.com/ine-rmotr-curriculum/freecodecamp-intro-to-pandas/blob/master/1%20-%20Pandas%20-%20Series.ipynb
