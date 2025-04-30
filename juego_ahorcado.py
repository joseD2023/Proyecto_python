#Juego EL ahorcado, mostrare mis capacidades 
import time 
import random
dibujo = [
["""

________
|      |
|      
|
|
|
|


"""],
["""

________
|      |
|      O
|
|
|
|

"""],
["""

________
|      |
|      O
|      |
|
|
|

"""],
["""

________
|      |
|      O
|     /|
|
|
|

"""],
["""

________
|      |
|      O
|     /|\\
|
|
|

"""],
["""

________
|      |
|      O
|     /|\\
|     /
|
|

"""],
["""

________
|      |
|      O
|     /|\\
|     / \\
|
|

"""]]


def mostrar_dibujo(parametro):
 dibujos_sucesivamente = dibujo[parametro]
 for draw in dibujos_sucesivamente:
  for draws in draw:
   print(draws, end="")
   print()

palabras = ["manzana", "carro", "moto"]
palabra_aleatoria = random.choice(palabras)
separar_letras = [texto for texto in palabra_aleatoria]
cantidad_letras = len(palabra_aleatoria)
intentos = 0
palabras_adivinadas = ""
lista_ver_letras = []
while intentos <= 8: 
  print("+--- BIENVENIDO AL JUEGO DEL AHORCADO ---+")

  print(f"Palabras Acertadas {lista_ver_letras}")
  palabra_adivinar = input("Ingrese una letra para adivinar: ")
  se_la_palabra = input("Si ya sabe la palabra, Ingresela aqui, si no de enter: ")
  if se_la_palabra == palabra_aleatoria:
   print(f"Excelente la palabra es {se_la_palabra}, Felicidades Ganaste!!")
   break
  if palabra_adivinar in separar_letras:
    palabras_adivinadas += palabra_adivinar
    print(f"Bien adivinaste una letra")
    lista_ver_letras.append(palabra_adivinar)
  else:
   print("La letra que ingreso No esta !!  ")
   mostrar_dibujo(intentos)
  time.sleep(3)
  intentos += 1


  
    


