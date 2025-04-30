#Ejercicio 2: Conversión de Temperatura
#Crea un programa que solicite al usuario una temperatura en grados Celsius y la convierta a grados Fahrenheit utilizando la fórmula Implementa excepciones para manejar posibles errores, como la introducción de caracteres no numéricos. El programa debe seguir pidiendo la entrada hasta que se proporcione un valor válido.

def conversion_fahrenheit(temperatura):
 temperatura = int(temperatura)
 formula = (temperatura * 9 / 5) + 32
 print(f"La conversión de {temperatura} Grados Celsius es {formula} Grados Fahrenheit")


while True: 
   print("+--- Ingreseo y salida del programa (si/no) ---+")
   opcion = input("Quiere Entrar o salir (si/no): ")
   if opcion.lower() == "si":
      try:
        celsius_usuario = int(input("Ingrese un temperatura: "))
        conversion_fahrenheit(celsius_usuario)
      except ValueError:
        print("Datos invalidos !!")
      except Exception as e: 
        print(f"Encontramos otro error broo {e}")
   elif opcion.lower() == "no":
     print("Gracias por utilizar neustro programa :3 ")
     break
   else:
    print("Ingrese una opcion valida porfavor:D ")