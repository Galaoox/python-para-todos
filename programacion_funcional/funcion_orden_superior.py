"""
El concepto de funciones de orden superior se refiere al uso de fun-
ciones como si de un valor cualquiera se tratara, posibilitando el pasar
funciones como parámetros de otras funciones o devolver funciones
como valor de retorno.

ejemplo:



def saludar(lang):
    def saludar_es():
        print("Hola")

    def saludar_en():
        print("Hello")

    def saludar_fr():
        pritn("salut")

    lang_func = {"es": saludar_es, "en": saludar_en, "fr": saludar_fr}

    return lang_func[lang]

f = saludar("es")
f()

Como podemos observar lo primero que hacemos en nuestro pequeño
programa es llamar a la función saludar con un parámetro “es” . En la
función saludar se definen varias funciones: saludar_es , saludar_en y
saludar_fr y a continuación se crea un diccionario que tiene como cla-
ves cadenas de texto que identifican a cada lenguaje, y como valores las
funciones. El valor de retorno de la función es una de estas funciones.
La función a devolver viene determinada por el valor del parámetro
lang que se pasó como argumento de saludar .
Como el valor de retorno de saludar es una función, como hemos
visto, esto quiere decir que f es una variable que contiene una función.
Podemos entonces llamar a la función a la que se refiere f de la forma
en que llamaríamos a cualquier otra función, añadiendo unos parénte-
sis y, de forma opcional, una serie de parámetros entre los paréntesis.
Esto se podría acortar, ya que no es necesario almacenar la función que
nos pasan como valor de retorno en una variable para poder llamarla:
>>> saludar(“en”)()
Hi
>>> saludar(“fr”)()
Salut
En este caso el primer par de paréntesis indica los parámetros de la
función saludar , y el segundo par, los de la función devuelta por salu-
dar .
"""