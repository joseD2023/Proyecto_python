parrafo = input("Ingrese un texto para No. Espacios y No. Letras: ")

def contar_espacio_palabras(parametro):
 contador_espacios = 0
 almancenar_datos = ""
 for espacios in parametro:
  if espacios == " ": #si encuentra un espacio en blanco lo ignora o lo salta y va contando 
   #cuantos espacios en blanco existen con el contador. 
   contador_espacios += 1
   continue
  else:  
   almancenar_datos += espacios
 letras = [texto for texto in almancenar_datos] #esto recorre el texto que viene junto ya que lo almacenamos en el 
 #variable almacenar datos. y de ahi lo aguarda dentro de esa lista y ya luego podemos saber cuantas letras existen.
 print(f"Las letras totales son: {len(letras)}")
 print(f"Espacios en blanco son: {contador_espacios}")

contar_espacio_palabras(parrafo)