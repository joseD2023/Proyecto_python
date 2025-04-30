#CODIGO DE PRUEBA DE UNA EXCEPTION EN PYTHON BASICA MAS GENERAL PARA CUALQUIER TIPO DE ERROR 

def error_text(numero):
   almacenar = numero * 2 
   print(f"El doble del numero: {numero} es {almacenar}")

while True: 
  try: 
    usuario_numero = int(input("Ingrese un numero porfavor: "))
    error_text(usuario_numero)
    break
  except ValueError:
    print("Error: Por favor, Ingrese un numero Valido")