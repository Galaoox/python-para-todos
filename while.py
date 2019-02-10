# while ejemplo
"""
contraseña = ""

while contraseña != "hannyker":
    contraseña = input("Ingrese su contraseña ")
    if contraseña == "hannyker":
        print("Ingreso exitoso")
    else:
        print("ingreso fallido, Intentelo de nuevo")


while True:
    pregunta = input("quiere salir del ciclo?")
    if pregunta == "si":
        break
    else:
        print("Seguira en el ciclo")
"""

edad = 0

while edad < 18:
    edad = edad + 1
    if edad % 2 == 0:
        continue
    print(f"Felicidades, tienes {str(edad)}")

#Es decir, con esta modificación el programa sólo
#imprimiría felicitaciones cuando la edad fuera impar.


















