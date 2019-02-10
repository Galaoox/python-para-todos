"""
Los diccionarios, también llamados matrices asociativas, deben su
nombre a que son colecciones que relacionan una clave y un valor. Por
ejemplo, veamos un diccionario de películas y directores:
"""

directores = {"love actually ": "richard curtis", "kill bill " : "Tarantino", "amelie " : "jean-pierre"}

"""
La diferencia principal entre los diccionarios y las listas o las tuplas es
que a los valores almacenados en un diccionario se les accede no por su
índice, porque de hecho no tienen orden, sino por su clave, utilizando
de nuevo el operador [] .
"""
print(directores["love actually "]) # devuelve “Richard Curtis”

"""
Al igual que en listas y tuplas también se puede utilizar este operador
para reasignar valores.
"""
directores["kill bill "] = "Hannyker"
print(directores["kill bill "])