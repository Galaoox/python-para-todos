"""
S.count(sub[, start[, end]])
Devuelve el número de veces que se encuentra sub en la cadena. Los
parámetros opcionales start y end definen una subcadena en la que
buscar.
S.find(sub[, start[, end]])
Devuelve la posición en la que se encontró por primera vez sub en la
cadena o -1 si no se encontró.
S.join(sequence)
Devuelve una cadena resultante de concatenar las cadenas de la se-
cuencia seq separadas por la cadena sobre la que se llama el método.
S.partition(sep)
Busca el separador sep en la cadena y devuelve una tupla con la sub-
cadena hasta dicho separador, el separador en si, y la subcadena del
separador hasta el final de la cadena. Si no se encuentra el separador, la
tupla contendrá la cadena en si y dos cadenas vacías.
S.replace(old, new[, count])
Devuelve una cadena en la que se han reemplazado todas las ocurren-
cias de la cadena old por la cadena new . Si se especifica el parámetro
count , este indica el número máximo de ocurrencias a reemplazar.
S.split([sep [,maxsplit]])
Devuelve una lista conteniendo las subcadenas en las que se divide
nuestra cadena al dividirlas por el delimitador sep . En el caso de que
54Revisitando objetos
no se especifique sep , se usan espacios. Si se especifica maxsplit , este
indica el número máximo de particiones a realizar.
"""