"""
Un objeto es una entidad que agrupa un
estado y una funcionalidad relacionadas.
El estado del objeto se define
a través de variables llamadas atributos, mientras que la funcionalidad
se modela a través de funciones a las que se les conoce con el nombre
de métodos del objeto.
una clase es una plantilla generica por la cual se pueden crear determinados objetos
las clases se definen pro medio de la palabra class seuguido del nombre de la clase
"""

class Coche:
    #Abstraccion de los objetos coche
    def __init__(self, gasolina):
        #atributos
        self.gasolina = gasolina
        print("Tenemos ", gasolina ," litros")
    
    def arrancar(self):
        #metodos
        if self.gasolina > 0:
            print("Arranca")
        else:
            print("No arranca")
    def conducir(self):
        #metodos
        if self.gasolina > 0:
            self.gasolina -= 1
            print("Quedan", self.gasolina, " litros")
        else:
            print("No se mueve")
        
mi_coche = Coche(3)

mi_coche.arrancar()

mi_coche.conducir()

mi_coche.conducir()

mi_coche.conducir()

mi_coche.arrancar()

