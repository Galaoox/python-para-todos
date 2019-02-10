"""
El modo de acceso puede ser cualquier combinación lógica de los
siguientes modos:
‘r’ :
read, lectura. Abre el archivo en modo lectura. El archivo tiene
que existir previamente, en caso contrario se lanzará una excepción
de tipo IOError .
‘w’ : write, escritura. Abre el archivo en modo escritura. Si el archi-
vo no existe se crea. Si existe, sobreescribe el contenido.
‘a’ : append, añadir. Abre el archivo en modo escritura. Se diferen-
cia del modo ‘w’ en que en este caso no se sobreescribe el conteni-
do del archivo, sino que se comienza a escribir al final del archivo.
‘b’ : binary, binario.
‘+’ : permite lectura y escritura simultáneas.
‘U’ : universal newline, saltos de línea universales. Permite trabajar
con archivos que tengan un formato para los saltos de línea que no
coincide con el de la plataforma actual (en Windows se utiliza el
caracter CR LF , en Unix LF y en Mac OS CR ).
"""

f = open("archivo.txt", "w")



while True:
    linea =f.readline()
    if not linea:
        break
    print(linea)


























