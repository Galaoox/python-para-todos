#transmitir ya sea un atributo o metodo a otra sub clase que lo utilize
class instrumento:
    def __init__(self, precio):
        self.precio = precio

    def tocar(self):
        #metodo
        print("Estamos tocando musica")
    
    def romper(self):
        print("Eso lo pagas tu ")
        print("Son ", self.precio, " $$$")

class bateria(instrumento):
    #al ingresar intrumento en los parentesis doy al orden de que los metodo y atributos de esa clase tambien puedan ser utilizados por esta clase
    pass

class Guitarra(instrumento):
    pass
"""
si se quiere añadir un metodo extra por ejemplo a guitarra 
se escribe un __init__ en la clase guitarra, esto se llama sobreescribir metodos
ene l caso de que queramos usar los metodos de isntrumento usamos un __init__(self,precio)
"""