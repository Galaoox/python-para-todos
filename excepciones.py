"""
las excepciones son errores detectados por python a la hora de ejecutar un programa, 
esto informa al usuario el error y detiene la ejecucion del programa.
ejemplo de una excepcion:


def division(a,b):
    return a / b
def calcular():
    division(1,0)

calcular()


EN python se utiliza try-except para capturar y tratar las excepciones
try define el fragmento de codigo en el que se podria generar la excepcion
except define el tratamiento que se ejecutara en caso de que exista la excepcion

try:
    f = fiel("archivo.txt")
except: 
    print("EL ARCHIVO NO EXISTE")

python permite usar varios except pero no varios try
ejemplo:

try:
    num =int("3a")
    print(no_existe)
except NameError:
    print("la variable no existe")
except ValueError:
    print("EL valor no es un numero")

tambien se puede usar un except para varios errores
ejemplo:


try:
    num =int("3a")
    print(no_existe)

except (NameError,ValueError):
    print("Ocurrio un error")

try-except tambien puede ir acompañado de un else en caso de que no se presente ninguna excepcion


try:
    numero = int(input("Ingrese un numero"))
except:
    print("Ocurrio un error")
else:
    print("Operacion exitosa")

tambien existe la clausula finally que siempre se ejecuta sin importar si hay excepciones o no
se suele utilizar para tareas de limpieza


try:
    z = x / y
except ZeroDivisionError:
    print("Division por cero")
finally:
    print("limpiando")

tambien se pueden crear excepciones propias
solo toca crear una clase y heredarle Exception y lanzarla con raise
ejemplo:

class Mierror(Exception):
    def __init__(self,valor):
        self.valor = valor
    
    def __str__(self):
        return "Error" + str(self.valor)

resultado = 33
try:
    if resultado > 20:
        raise Mierror(resultado)
except Mierror:
    print("error")

lista de excepciones:

BaseException :
Clase de la que heredan todas las excepciones.
Exception(BaseException) : Super clase de todas las excepciones que
GeneratorExit(Exception) : Se pide que se salga de un generador.
no sean de salida.
StandardError(Exception) :
Clase base para todas las excepciones que
no tengan que ver con salir del intérprete.
ArithmeticError(StandardError) :
ticos.
Clase base para los errores aritmé-
FloatingPointError(ArithmeticError) :
coma flotante.
OverflowError(ArithmeticError) :
poder representarse.
Error en una operación de
Resultado demasiado grande para
ZeroDivisionError(ArithmeticError) :
Lanzada cuando el segundo
argumento de una operación de división o módulo era 0.
AssertionError(StandardError) : Falló la condición de un estamento
AttributeError(StandardError) : No se encontró el atributo.
assert .
68Excepciones
EOFError(StandardError) :
Se intentó leer más allá del final de fichero.
EnvironmentError(StandardError) :
nados con la entrada/salida.
Clase padre de los errores relacio-
IOError(EnvironmentError) : Error en una operación de entrada/salida.
OSError(EnvironmentError) : Error en una llamada a sistema.
WindowsError(OSError) :
Error en una llamada a sistema en Windows.
ImportError(StandardError) :
No se encuentra el módulo o el elemen-
to del módulo que se quería importar.
LookupError(StandardError) :
IndexError(LookupError) :
rango posible.
KeyError(LookupError) :
El índice de la secuencia está fuera del
La clave no existe.
MemoryError(StandardError) :
NameError(StandardError) :
nombre.
Clase padre de los errores de acceso.
No queda memoria suficiente.
No se encontró ningún elemento con ese
UnboundLocalError(NameError) :
variable.
El nombre no está asociado a ninguna
ReferenceError(StandardError) :
cia fuerte apuntando hacia él.
RuntimeError(StandardError) :
cificado.
El objeto no tiene ninguna referen-
Error en tiempo de ejecución no espe-
NotImplementedError(RuntimeError) :
implementado.
SyntaxError(StandardError) :
Ese método o función no está
Clase padre para los errores sintácticos.
69Python para todos
IndentationError(SyntaxError) :
Error en la indentación del archivo.
TabError(IndentationError) : Error debido a la mezcla de espacios y
SystemError(StandardError) : Error interno del intérprete.
tabuladores.
TypeError(StandardError) : Tipo
de argumento no apropiado.
ValueError(StandardError) : Valor
UnicodeError(ValueError) :
con unicode.
del argumento no apropiado.
Clase padre para los errores relacionados
UnicodeDecodeError(UnicodeError) : Error de decodificación unicode.
UnicodeEncodeError(UnicodeError) : Error de codificación unicode.
UnicodeTranslateError(UnicodeError) :
StopIteration(Exception) :
Warning(Exception) :
Error de traducción unicode.
Se utiliza para indicar el final del iterador.
Clase padre para los avisos.
DeprecationWarning(Warning) :
rísticas obsoletas.
Clase padre para avisos sobre caracte-
FutureWarning(Warning) : Aviso. La semántica de la construcción cam-
ImportWarning(Warning) : Aviso sobre posibles errores a la hora de
biará en un futuro.
importar.
PendingDeprecationWarning(Warning) :
Aviso sobre características que
se marcarán como obsoletas en un futuro próximo.
RuntimeWarning(Warning) :
tiempo de ejecución.
Aviso sobre comportmaientos dudosos en
70Excepciones
SyntaxWarning(Warning) :
Aviso sobre sintaxis dudosa.
UnicodeWarning(Warning) :
Aviso sobre problemas relacionados con
Unicode, sobre todo con problemas de conversión.
UserWarning(Warning) :
mador.
Clase padre para avisos creados por el progra-
KeyboardInterrupt(BaseException) :
por el usuario.
SystemExit(BaseException) :
ejecución.
El programa fué interrumpido
Petición del intérprete para terminar la ejecucions
"""
