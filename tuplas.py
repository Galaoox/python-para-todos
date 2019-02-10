#se utilizan paréntesis en lugar de corchetes.

tupla1 = (1,2,3,True,"Juan")

"""
En realidad el constructor de la tupla es la coma, no el paréntesis, pero
el intérprete muestra los paréntesis, y nosotros deberíamos utilizarlos,
por claridad.

Además hay que tener en cuenta que es necesario añadir una coma
para tuplas de un solo elemento, para diferenciarlo de un elemento
entre paréntesis.
"""
tupla_sencilla = (1,)

"""
Para referirnos a elementos de una tupla, como en una lista, se usa el
operador [] :
"""

variable1 = tupla1[0]
variable2 = tupla1[0:2]

"""
Podemos utilizar el operador [] debido a que las tuplas, al igual que
las listas, forman parte de un tipo de objetos llamados secuencias.

Además son inmutables, es decir, sus valores no se pueden modificar
una vez creada; y tienen un tamaño fijo.
"""