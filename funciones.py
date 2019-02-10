"""
Una función es un fragmento de código con un nombre asociado que
realiza una serie de tareas y devuelve un valor.
ejemplo de como declarar una funcion
lo que esta dentro del parentesis son los valores que acepta la funcion


def mi_funcion(valor1,valor2):
    print(valor1)
    print(valor2)





def multiplicar(numero1,numero2,numero3):
    #ejemplo de funcion que multiplica tres numeros y imprime el resultado
    resultado = 0
    resultado = numero1 * numero2 * numero3
    print(f"El resultado de la operacion es {resultado}")


variable1 = int(input("ingrese un numero "))
variable2 = int(input("ingrese un numero "))
variable3 = int(input("ingrese un numero "))

multiplicar(variable1,variable2,variable3)


def imprimir(texto, veces = 1):
    #el valor veces determina cuantas veces se imprimira el texto
    print(veces * texto)

imprimir(" ja ",5)

Para definir funciones con un número variable de argumentos coloca-
mos un último parámetro para la función cuyo nombre debe preceder-
se de un signo * :

def varios(param1,param2, *otros):
    #se puede evitar el nombre "otros" y poner **
    for repetir in otros:
        print(repetir)
        print(" ")

varios(1,2)
varios(1,2,3)
varios(1,2,3,4)

def varios(param1,param2, **otros):
    #ene ste caso se guarda en un diccionario el valor otros
    for i in otros.items():
        print(i)
        print(" ")
varios(1,2, tres = 3)

#al pasar una tupla como valor lo que haria python es crear una nueva instancia




def funcion(x, y):
    x = x + 3
    y.append(23)
    #append sirve para añadir objetos a una lista en este caso y
    print(x, y)

x = 22
y =[22]

funcion(x, y) #25 [22, 23]
print(x, y) #22 [22, 23]
#al ejecutarse la funcion se nota que la varible x no guarda el dato que se genera en la funcion


Como vemos esta función tan sencilla no hace otra cosa que sumar los
valores pasados como parámetro y devolver el resultado como valor de
retorno.


def sumar(x,y):
    return x + y
print(sumar(5, 5)) # 10
tambien se pueden pasar varios valores si se usa la "," para separarlos
"""
