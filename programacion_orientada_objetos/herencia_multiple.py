"""
En el caso que se quiera heredar de varias clases algun metodo o lo que sea, se usa esta sintaxis, ejemplo:
class cocodrilo(terrestre,acuatico):
    pass
en el caso de que las clases padre tengan un metodo o atributo parecido se sobreescribirian los procesos
que esten mas a la derecha
"""


class terrestre:
    def desplazar(self):
        print("El animal anda")


class acuatico:
    def desplazar(self):
        print("El animal nada")


class cocodrilo(terrestre, acuatico):
    pass


c = cocodrilo()

c.desplazar()
