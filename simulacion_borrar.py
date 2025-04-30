#JUEGO DE LA RAYA 
import time 
dibujo_cuadrante = [
    [" ", " ", "x"],
    [" ", "x", " "],
    ["x", " ", " "]
]

import time 

def verificacion_en_linea():
    for matriz in dibujo_cuadrante:
        if matriz[0] == matriz[1] == matriz[2]:
            print("Has ganado en filas")
            break 

def verificacion_en_columnas():
    for columnas in range(3):
        if dibujo_cuadrante[0][columnas] == dibujo_cuadrante[1][columnas] == dibujo_cuadrante[2][columnas]:
            print("Has ganado en columnas")
            break 

def verificacion_diagonal():
    if dibujo_cuadrante[0][0] == dibujo_cuadrante[1][1] == dibujo_cuadrante[2][2]:
        print("Gano El jugador en diagonal")
    if dibujo_cuadrante[0][2] == dibujo_cuadrante[1][1] == dibujo_cuadrante[2][0]:
        print("Gano el Jugador en diagonal")

verificacion_en_linea()
verificacion_en_columnas()
verificacion_diagonal()





def ganamos():
# Verificar si todas las letras de la primera columna son iguales
   if dibujo_cuadrante[0][0] == dibujo_cuadrante[0][1] == dibujo_cuadrante[0][2]:
       print("Tiene la misma letra en la primera fila")
   elif dibujo_cuadrante[1][0] == dibujo_cuadrante[1][1] == dibujo_cuadrante[1][2]: 
       print("Tiene la misma letra en la segunda fila")
   elif dibujo_cuadrante[2][0] == dibujo_cuadrante[2][1] == dibujo_cuadrante[2][2]:
       print("Tiene la misma letra en la tercera fila")
   elif dibujo_cuadrante[0][0] == dibujo_cuadrante[1][1] == dibujo_cuadrante[2][2]:
       print("La diagonal principal es esta")
   elif dibujo_cuadrante[0][2] == dibujo_cuadrante[1][1] == dibujo_cuadrante[2][0]:
       print("Diagonal secudnaria")
   elif dibujo_cuadrante[0][0] == dibujo_cuadrante[1][0] == dibujo_cuadrante[2][0]:
        print("Columna 1")
   elif dibujo_cuadrante[0][1] == dibujo_cuadrante[1][1] == dibujo_cuadrante[2][1]:
       print("columna 2")
   elif dibujo_cuadrante[0][2] == dibujo_cuadrante[1][2] == dibujo_cuadrante[2][2]:
       print("Columna 3")
   else:
       print("No tiene la misma letra en la primera columna")


        


  
 