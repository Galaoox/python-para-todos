class personaje:
    def __init__(self, vida, daño, defensa):
        #atributos basicos del personaje

        self.vida = vida
        print("El personaje tiene ", vida , " puntos de vida")

        self.daño = daño
        print("El personaje tiene ", daño , " puntos de daño")
        
        self.defensa = defensa
        print("El personaje tiene ", defensa , " puntos de defensa")
    
    def atacar(self):
        #metodos
        if self.vida > 0 :
            print("El personje ataca")
        else:
            print("EL personjae murio")
    
    def defender(self):
        #metodos
        if self.defensa > 0 :
            print("El personje se defiende")
        else:
            print("EL personjae murio")

    def curarse(self):
        #metodos
        if self.vida > 0 :
            self.vida = vida + 5
            print("El personje se cura")
        else:
            print("EL personjae murio")
