import threading
import time

# Función que imprime números del 1 al 5
def imprimir_numeros():
    for numero in range(1, 6):
        print(f"Número: {numero}")
        time.sleep(1)

# Función que imprime letras A, B, C
def imprimir_letras():
    letras = ['A', 'B', 'C']
    for letra in letras:
        print(f"Letra: {letra}")
        time.sleep(1)

# Crear dos hilos y asignarles las funciones
hilo_numeros = threading.Thread(target=imprimir_numeros)
hilo_letras = threading.Thread(target=imprimir_letras)

# Iniciar ambos hilos
hilo_numeros.start()
hilo_letras.start()

# Esperar a que ambos hilos terminen antes de continuar
hilo_numeros.join()
hilo_letras.join()

# Mensaje final después de que ambos hilos hayan terminado
print("Hilos terminaron. Programa principal finalizado.")
