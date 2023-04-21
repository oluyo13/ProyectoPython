import pandas as pd
import numpy as np


#Crear la base de datos
df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

df

df.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]

df

#Para saber el tipo de datos .dtypes
df.dtypes
df.dtypes.value_counts()

#Si queremos saber todos los valores de la columna para un individuo
df.loc['Canada']
df.iloc[-1] #Por posicion

#Por columna
df['Population']
df[['Population', 'GDP']]
df[1:3]

#De francia a Italia, poblacion
df.loc['France': 'Italy', 'Population']

#Condicionales
df.loc[df['Population'] > 70, 'Population']
df.loc[df['Population'] > 70, ['Population', 'GDP']]

#Funcion drop para eliminar (No mostrar)
df.drop('Canada')
df.drop(['Canada', 'Japan'])
df.drop(columns=['Population', 'HDI'])

#OPERACIONES
df[['Population', 'GDP']]
df[['Population', 'GDP']] / 100

#Se puede generar una variable
crisis = pd.Series([-1_000_000, -0.3], index=['GDP', 'HDI'])
crisis

#Y sumar a la tabla df anterior
df[['GDP', 'HDI']] + crisis

#Para crear una nueva columna'''''''''''''''''''''''''''''''''''''
langs = pd.Series(
    ['French', 'German', 'Italian'],
    index=['France', 'Germany', 'Italy'],
    name='Language'
)

df['Language'] = langs
df

#Poner todo en ingles
df['Language'] = 'English'

#Renombrar las colimnas
df.rename(
    columns={
        'HDI': 'Human Development Index',
        'Anual Popcorn Consumption': 'APC'
    }, index={
        'United States': 'USA',
        'United Kingdom': 'UK',
        'Argentina': 'AR'
    })


#Para crear una nueva columna:
df['GDP Per Capita'] = df['GDP'] / df['Population']
df


population = df['Population']
population.min(), population.max()
population.sum()
population.sum() / len(population)
population.mean()
population.std()
population.median()
population.describe()
population.quantile(.25)
population.quantile([.2, .4, .6, .8, 1])



#Data: https://github.com/ine-rmotr-curriculum/freecodecamp-intro-to-pandas/blob/master/3%20-%20Pandas%20-%20DataFrames.ipynb



