"""
usando __doc__ se documenta
"""
import pydoc

#pydoc.py(nombre1 [nombre2 ...])










def haz_algo(arg):
    """Este es el docstring de la funcion."""
    print (arg)
print (haz_algo.__doc__)
haz_algo.__doc__ = """Este es un nuevo docstring."""
print (haz_algo.__doc__)