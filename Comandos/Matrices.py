#Primero debemos importar numpy 
import numpy as np

'Podemos definir una matriz de la siguiente manera con el comando array'
np.array([1,2,3,4])

'Podemos crear variables o coeficientes'
a = np.array([1,2,3,4])
b = np.array([0,.5,1,1.5])

#Si queremos ver lo que hemos creado solo escribimos la variable
a
b

'Podemos pedirle cierto valores de la matriz'
a[0],a[1] #Aqui estamos pidiendo el valor 0 y 1 de la matriz a
a[0:]  #Aqui estamos pidiendo el primer valor y todos los demas
a[1:3] #pedimos el índice 1 y el índice 2 (pero sin incluir el índice 3)
'Para pedir el ultimo elemento podemos pedir la posicion .1'
a[-1]

'Si queremos saber el tipo de dato almacenado usamos dtype'
a.dtype
b.dtype

#Podemos crar matrices mas grandes
A = np.array([
    [1,2,3],
    [4,5,6]]
)

'Para pedir la dimension de la matriz usamos shape'
A.shape
a.shape
b.shape

'Se puede pedir dimensiones con ndim'
A.ndim

'Para pedir cuanto datos tiene usamos size'
A.size

#Operaciones con matrices
a+10
a*10 
a+=100
a+b

#Crear numeros aleatoreos
'Dos numeros aleatoreos con distribucion aleatorea'
np.random.random(size=2)
'Dos numeros con distribucion normal, media 0 y dsv 1'
np.random.normal(size=2)
'Crear matriz de 2x4 con numeros entre 0 y 1'
np.random.rand(2, 4)

'Crear una lista de 0 hasta 9'
np.arange(10)
'Crear una lista de 5 hasta 9'
np.arange(5, 10)
'Crear una lista de 0 hasta 4.9, pero yendo de 0.1 en 0.1'
np.arange(0, 5, .1)

'Genera 5 numeros entre 0 y 1, con numero equisdistantes'
np.linspace(0, 1, 5)

#Valores de ceros, unos y vacios
np.zeros(5)
np.zeros((3, 3))
np.ones(5)
np.ones((3, 3))
np.empty(5)
np.empty((2, 2))

