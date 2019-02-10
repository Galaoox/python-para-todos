"""
L.append(object)
Añade un objeto al final de la lista.
L.count(value)
Devuelve el número de veces que se encontró value en la lista.
L.extend(iterable)
Añade los elementos del iterable a la lista.
L.index(value[, start[, stop]])
Devuelve la posición en la que se encontró la primera ocurrencia de
value . Si se especifican, start y stop definen las posiciones de inicio y
fin de una sublista en la que buscar.
L.insert(index, object)
Inserta el objeto object en la posición index .
L.pop([index])
Devuelve el valor en la posición index y lo elimina de la lista. Si no se
especifica la posición, se utiliza el último elemento de la lista.
L.remove(value)
Eliminar la primera ocurrencia de value en la lista.
L.reverse()
Invierte la lista. Esta función trabaja sobre la propia lista desde la que
se invoca el método, no sobre una copia.
L.sort(cmp=None, key=None, reverse=False)
Ordena la lista. Si se especifica cmp , este debe ser una función que tome
como parámetro dos valores x e y de la lista y devuelva -1 si x es menor
que y , 0 si son iguales y 1 si x es mayor que y .
El parámetro reverse es un booleano que indica si se debe ordenar
la lista de forma inversa, lo que sería equivalente a llamar primero a
L.sort() y después a L.reverse() .
55Python para todos
Por último, si se especifica, el parámetro key debe ser una función que
tome un elemento de la lista y devuelva una clave a utilizar a la hora de
comparar, en lugar del elemento en si.
"""