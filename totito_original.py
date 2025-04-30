#JUEGO DE LA RAYA 
dibujo_cuadrante = [
    ["|____|", "|____|", "|____|"],
    ["|____|", "|____|", "|____|"],
    ["|____|", "|____|", "|____|"]
 ]
 
def dibujar_cuadrante_raya():
    for fila in dibujo_cuadrante:
        print("".join(fila))

def figura_valida(validacion):
    validacion = validacion.upper()
    return validacion in ["X", "O"]

def verificacion_en_linea():
    for fila in dibujo_cuadrante:
        if fila[0] == fila[1] == fila[2] and fila[0].strip() != '|____|':
            return True
    return False

def verificacion_en_columnas():
    for col in range(3):
        if dibujo_cuadrante[0][col] == dibujo_cuadrante[1][col] == dibujo_cuadrante[2][col] and dibujo_cuadrante[0][col] != '|____|':
            return True
    return False

def verificacion_diagonal():
    if dibujo_cuadrante[0][0] == dibujo_cuadrante[1][1] == dibujo_cuadrante[2][2] and dibujo_cuadrante[0][0] != '|____|':
        return True
    if dibujo_cuadrante[0][2] == dibujo_cuadrante[1][1] == dibujo_cuadrante[2][0] and dibujo_cuadrante[0][2] != '|____|':
        return True
    return False

def hay_ganador():
    return verificacion_en_linea() or verificacion_en_columnas() or verificacion_diagonal()

def hay_empate():

    for fila in dibujo_cuadrante:
        if "|____|" in fila:
            return False  # Si alguna fila tiene "|____|", aún hay lugares vacíos
    return True  

dibujar_cuadrante_raya()

def reiniciar_juego():
    global dibujo_cuadrante
    dibujo_cuadrante = [
        ["|____|", "|____|", "|____|"],
        ["|____|", "|____|", "|____|"],
        ["|____|", "|____|", "|____|"]
    ]


def jugar_de_nuevo():

 while True:
    posiciones_x = input("Introduce la coordenada X del 1 al 3: ")
    posiciones_y = input("Introduce la coordenada Y del 1 al 3: ")
    figura_usar = input("Introduce 0 para círculo o X para cruz:")

    try:
        if posiciones_x.isdigit() and posiciones_y.isdigit() and 1 <= int(posiciones_x) <= 3 and 1 <= int(posiciones_y) <= 3:
            if dibujo_cuadrante[int(posiciones_x) - 1][int(posiciones_y) - 1].strip() == "|____|" and figura_valida(figura_usar):
                posiciones_x = int(posiciones_x) - 1
                posiciones_y = int(posiciones_y) - 1
                dibujo_cuadrante[posiciones_x][posiciones_y] = f"| {figura_usar}  |"
                dibujar_cuadrante_raya()

                if hay_ganador():
                    print(f"¡Felicidades! Ganó el jugador con {figura_usar}.")
                    opcion = input("Quieres jugar de nuevo (si/no): ")
                    if opcion.lower() == "si":
                        reiniciar_juego()
                        dibujar_cuadrante_raya()
                        jugar_de_nuevo()
                    elif opcion.lower() == "no":
                        break 
                    else: 
                       print("Opcion invalida!!!")
                elif hay_empate():
                    print("¡Empate! No hay más movimientos posibles.")
                    opcion = input("Quieres jugar de nuevo (si/no): ")
                    if opcion.lower() == "si":
                        reiniciar_juego()
                        dibujar_cuadrante_raya() 
                        jugar_de_nuevo()
                    else: 
                       break
            else:
                print("El lugar ya está ocupado o la figura no es válida. Vuelve a intentar.")
        else:
            print("El número que ingresó está fuera de límites!!!")
    except IndexError:
        print("¡Error, Existe algún Error!")

jugar_de_nuevo()



