"""
Números, como pueden ser 3 (entero) , 15.57 (de coma flotante) o 7 + 5j (complejos)
Cadenas de texto, como “Hola Mundo”
Valores booleanos: True (cierto) y False (falso).
"""
# esto es una cadena
c = ("Hola Mundo")
# y esto es un entero
e = 23
# podemos comprobarlo con la función type
type(c)
type(e)
"""
type toma cualquier cosa y devuelve su tipo. Y quiero decir cualquier cosa: enteros, cadenas, 
listas, diccionarios, tuplas, funciones, clases, módulos, incluso tipos.
El tipo long de Python permite almacenar números de cualquier preci-
sión, estando limitados solo por la memoria disponible en la máquina.
Al asignar un número a una variable esta pasará a tener tipo int , a
menos que el número sea tan grande como para requerir el uso del tipo
long .
"""
# type(entero) devolvería int
entero = 23
"""
También podemos indicar a Python que un número se almacene usan-
do long añadiendo una L al final:

type(entero) devolvería long
entero = 23L

El literal que se asigna a la variable también se puede expresar como
un octal, anteponiendo un cero:

# 027 octal = 23 en base 10
entero = 027
o bien en hexadecimal, anteponiendo un 0x:
# 0×17 hexadecimal = 23 en base 10
entero = 0×17    

Para representar un número real en Python se escribe primero la parte
entera, seguido de un punto y por último la parte decimal."""
real = 0.2703
real = 0.1e-3
#salto de linea
triple = ("hola\n como estan")
print(triple)

#operador logico (and,or,not)
r = True and False #false
t = True or False #True
p = not True    #false
