"""
Listas: La lista es un tipo de colección ordenada. Sería equivalente a lo que en
otros lenguajes se conoce por arrays, o vectores.
Las listas pueden contener cualquier tipo de dato
Ejemplo:
"""
l = [22, True, "una lista", [1, 2]]

"""Podemos acceder a cada uno de los elementos de la lista escribiendo el
nombre de la lista e indicando el índice del elemento entre corchetes.
Ten en cuenta sin embargo que el índice del primer elemento de la
lista es 0, y no 1:"""

variable1 = l[0]

"""Si queremos acceder a un elemento de una lista incluida dentro de otra
lista tendremos que utilizar dos veces este operador, primero para in-
dicar a qué posición de la lista exterior queremos acceder, y el segundo
para seleccionar el elemento de la lista interior:"""

variable2 = l[3][1]

#modificar
l[0] = 5

#acceder a una parte de la lista de un lado hasta el otro
variable3 = l[0:3]

#acceder a una aparte de la lista pero saltarse un pedazo
variable4 = l[0:4:2] # mi_var vale [99, “una lista”]

"""Hay que mencionar así mismo que no es necesario indicar el principio
y el final del slicing, sino que, si estos se omiten, se usarán por defecto
las posiciones de inicio y fin de la lista, respectivamente:"""
variable5 = l[1:] # mi_var vale [5, “una lista”]

#También podemos utilizar este mecanismo para modificar la lista:


l[0:2] = [0, 1] 