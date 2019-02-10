"""

__init__(self, args)
Método llamado después de crear el objeto para realizar tareas de
inicialización.

__new__(cls, args)
Método exclusivo de las clases de nuevo estilo que se ejecuta antes que
__init__ y que se encarga de construir y devolver el objeto en sí. Es
equivalente a los constructores de C++ o Java. Se trata de un método
estático, es decir, que existe con independencia de las instancias de
la clase: es un método de clase, no de objeto, y por lo tanto el primer
parámetro no es self , sino la propia clase: cls .

__del__(self)
Método llamado cuando el objeto va a ser borrado. También llamado
destructor, se utiliza para realizar tareas de limpieza.

__str__(self)
Método llamado para crear una cadena de texto que represente a nues-
tro objeto. Se utiliza cuando usamos print para mostrar nuestro objeto
o cuando usamos la función str(obj) para crear una cadena a partir de
nuestro objeto.

__cmp__(self, otro)
Método llamado cuando se utilizan los operadores de comparación
para comprobar si nuestro objeto es menor, mayor o igual al objeto
pasado como parámetro. Debe devolver un número negativo si nuestro
objeto es menor, cero si son iguales, y un número positivo si nuestro
objeto es mayor. Si este método no está definido y se intenta com-
parar el objeto mediante los operadores < , <= , > o >= se lanzará una
excepción. Si se utilizan los operadores == o != para comprobar si dos
objetos son iguales, se comprueba si son el mismo objeto (si tienen el
mismo id).

__len__(self)
Método llamado para comprobar la longitud del objeto. Se utiliza, por
ejemplo, cuando se llama a la función len(obj) sobre nuestro objeto.
Como es de suponer, el método debe devolver la longitud del objeto.

"""