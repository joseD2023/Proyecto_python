def divide():
 while True: 
  try:
    op1 = float(input("Introduce el primer numero: "))
    op2 = float(input("Introduce el segundo numero: "))
    print(f"La division es: {op1/op2}")
    break
  except ValueError:
    print("El valor introduccido es Erroneo.")
  except ZeroDivisionError:
   print("No se puede dividir entre cero.")
  except Exception as e:
            print(f"Error inesperado: {e}")
 print("Calculos finalizados")

divide()