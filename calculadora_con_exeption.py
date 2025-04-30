#Ejercicio 1: Calculadora Simple con Excepciones
#Crea una calculadora simple que solicite al usuario dos números y una operación (+, -, *, /). Implementa excepciones para manejar posibles errores, como la introducción de caracteres no numéricos o la división por cero. La calculadora debe seguir pidiendo la entrada hasta que se proporcionen valores y operadores válidos.

def calculadora(operacion, numero1, numero2):
    opcion = int(operacion)
    
    if opcion == 1:
        resultado = numero1 + numero2
        print(f"El resultado de la operación es: {resultado}")
    elif opcion == 2: 
        resultado = numero1 - numero2
        print(f"El resultado de la operación es: {resultado}")
    elif opcion == 3:
        resultado = numero1 * numero2
        print(f"El resultado de la operación es: {resultado}")
    elif opcion == 4:
        if numero2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = numero1 / numero2
            print(f"El resultado de la operación es: {resultado}")
    else: 
        print("Ingrese un operador válido.")

while True:
    print("+--- Bienvenido a mi calculadora sin Errores ---+")
    print("+--- Elija un Operador aritmético           ---+")
    print("+--- 1. Suma                                ---+")
    print("+--- 2. Resta                               ---+")
    print("+--- 3. Multiplicación                      ---+")
    print("+--- 4. División                            ---+")
    print("+--- 5. Salir                               ---+")
    
    try: 
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese otro número: "))
        operador = int(input("Ingrese una opción: "))
        
        if operador == 5:
            print(f"Usted ha ingresado los números {num1}, {num2}, pero seleccionó la opción 'Salir'.")
            print("Gracias por utilizar el programa")
            break
        else:
            calculadora(operador, num1, num2)
    except ValueError:
        print("Usted ha ingresado texto en lugar de números.")


 
 

 
 
