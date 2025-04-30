ingrese_palabra = input("Ingrese una palabra: ")

def invertir_texto(palabra):
 almacenar = " "
 ingrese_palabra = palabra
 for secuencia in ingrese_palabra[::-1]:
  almacenar += secuencia 
 print(almacenar)

invertir_texto(ingrese_palabra)