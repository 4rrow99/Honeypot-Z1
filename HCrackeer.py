import hashlib

hash_file = "Ingrese el hash"

dic_file = input("ingrese la direccion del diccionario: ")

with open(dic_file, 'r') as file:

    diccionario = [line.stip() for line in file]

    for password in diccionario:

        hash_calculado = hashlib.sha256(password.encode()).hexdigest()

        if hash_calculado == hash_file:

            print("la contrasena original es: " + password)
            break
        else: 
            print("la contrasena no se encuentra en el diccionario")

    