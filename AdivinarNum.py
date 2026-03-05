import random

MINIMO = 1
MAXIMO = 10

numero_azar = random.randint(MINIMO, MAXIMO)
intentos = 0

while True:
    intento_usuario = int(input("Introduce un numero: "))
    intentos += 1 
    if intento_usuario > numero_azar:
        print("Error el numero es mas pequeno que " + str
        (intento_usuario))
    elif intento_usuario < numero_azar:
        print("Error el numero es mas grande que  " + str
        (intento_usuario))
    else:
       break 
print("Has acertado")