import tkinter as tk
import pyttsx3 as yt
import speech_recognition as sr
import webbrowser
from googleapiclient.discovery import build

# Inicializar el motor de síntesis de voz
comando_voz = yt.init()
comando_voz.setProperty('rate', 150)

# Definir la función para buscar videos de YouTube
def buscar_videos_youtube(consulta):
    API_KEY = 'AIzaSyAbU8maWnEUb1tgLWRuO22aOwUC0Mib2eo'
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    request = youtube.search().list(
        q=consulta,
        part='snippet',
        type='video',
        maxResults=1
    )
    response = request.execute()

    if 'items' in response:
        video_id = response['items'][0]['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        webbrowser.open(video_url)
    else:
        print("No se encontraron videos para la consulta:", consulta)

# Definir la función para escuchar y procesar la voz
def Microphone():
    global salir
    reconocer_voz = sr.Recognizer()

    with sr.Microphone() as source:
        print("Escuchando....")
        audio = reconocer_voz.listen(source)

    try:
        texto_voz = reconocer_voz.recognize_google(audio, language='es-ES')
        if texto_voz.lower() == "detener":
            salir = True  
            return salir 
        computadora_habla("Vamos a YouTube a buscar: " + texto_voz)
        print("Vamos a YouTube a buscar: " + texto_voz)
        buscar_videos_youtube(texto_voz)
    except:
        computadora_habla("Lo siento, no te he entendido.")

# Definir la función para que la computadora hable
def computadora_habla(frase):
    comando_voz.say(str(frase))
    comando_voz.runAndWait()

# Definir la función para encender el micrófono
def encender_microfono():
    computadora_habla("Has encedido el Microfono.")
    Microphone()

# Definir la función para apagar el micrófono y salir del programa
def apagar_microfono():
    global salir
    salir = True
    computadora_habla("Has Muteado El Microfono.")

# Crear la ventana de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Control de Micrófono")
ventana.geometry("800x800")

# Crear botones para encender y apagar el micrófono
boton_encender = tk.Button(ventana, text="Encender Micrófono", command=encender_microfono)
boton_encender.pack(pady=10)

boton_apagar = tk.Button(ventana, text="Apagar Micrófono", command=apagar_microfono)
boton_apagar.pack(pady=5)

# Variable para controlar el estado del programa
salir = False

# Loop principal de la interfaz gráfica
ventana.mainloop()
