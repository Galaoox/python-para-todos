"""
la serializacion sirve para guardar un archivo que se piensa guardar un largo 
tiempo
cpickle es mas rapido por lo que siempre se usara
"""

try:
    import cpickle as pickle
except ImportError:
    import pickle


fichero = open("dato.dat", "w")
animales = ["piton", "mono", "camello"]

pickle.dump(animales, fichero, 2)

fichero.close()

"""
la forma mas sencilla de serializar u objeto usando pickle es mediante
el metodo dump
"""