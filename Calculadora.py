def calculadora(num1, num2, op):
    if op == 1:
        print(f"El resultado de la suma de {num1} y {num2}: {num1 + num2}")
    elif op == 2:
        print(f"El resultado de la resta de {num1} y {num2}: {num1 - num2}")
    elif op == 3:
        print(f"El resultado de la multiplicacion de {num1} y {num2}: {num1 * num2}")
    elif op == 4:
        print(f"El resultado de la divicion de {num1} y {num2}: {num1 / num2}")
    else: 
        print(" Error opcion incorecta")
calculadora(45,32,1)
calculadora(45,32,2)
calculadora(45,32,3)
calculadora(45,32,4)