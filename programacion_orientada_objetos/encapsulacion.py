"""
La encapsulacion se refiere a impedir el acceso a determinados metodos y atributos de un
objeto estableciendo si se pueden usar desde fuera de la clase  
en python no existen los modificadores de acceso, lo que se suele hacer es escribir en una variable o 
funcion dos guiones __ejemplo   esto hace a la variable o funcion privada



class Ejemplo:
    def publico(self):
        print("Publico")

    def __privado(self):
        print("Privado")


ejemplo1 = Ejemplo()

ejemplo1.publico()

ejemplo1._Ejemplo__privado()


en si al usar ese metodo no vuelve completamente privada la funcion o variable
ya que se puede acceder a esta por medio de lo siguiente: ejemplo1._Ejemplo__privado()

en el caso de que se quiera hacer de forma controlada, se puede hacer como getVariable y setVariable
tambien esto es conocido como getters y setters


class Fecha():
    def __init__(self):
        self.__dia = 1
    
    def getDia(self):
        return self.__dia
    
    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia =dia
        else:
            print("ERROR")

mi_fecha = Fecha()
mi_fecha.setDia(33)

"""

class Fecha (object):
    def __init__(self):
        self.__dia = 1

    def getDia(self):
        return self.__dia
    
    def setDia(self, dia):
        if dia > 0 and dia <= 31:
            self.__dia = dia
        else:
            print("EROR")
    dia = property(getDia, setDia)

mi_fecha = Fecha()
mi_fecha.dia = 33 