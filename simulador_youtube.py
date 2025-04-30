import pyttsx3 as yt
import speech_recognition as sr
import time 
import webbrowser  # Importar el módulo webbrowser para abrir el navegador
from googleapiclient.discovery import build  # Importar la función build del módulo discovery de la biblioteca googleapiclient

comando_voz = yt.init()
comando_voz.setProperty('rate', 150)
#----------------------------------------------------------- Bibliotecas Arrbia -----------------------------------
#Vamos a implementar el codigo para que cuando le pidamos algo por medio de voz esta nos abra youtube y podamos escuhar musica 

# Definir una función para buscar videos de YouTube de un artista o banda
def buscar_videos_youtube(consulta):
    API_KEY = 'AIzaSyAbU8maWnEUb1tgLWRuO22aOwUC0Mib2eo'  # Definir la clave de la API de YouTube
    youtube = build('youtube', 'v3', developerKey=API_KEY)  # Construir un objeto de servicio para interactuar con la API de YouTube

    # Realizar la búsqueda de videos en YouTube con la consulta proporcionada
    request = youtube.search().list(
        q=consulta,  # Consulta de búsqueda
        part='snippet',  # Parte de los resultados que se devolverán (en este caso, los datos del video)
        type='video',  # Tipo de resultado (en este caso, queremos videos)
        maxResults=1  # Número máximo de resultados que se devolverán (en este caso, queremos solo el primer resultado)
    )
    response = request.execute()  # Ejecutar la solicitud de búsqueda y obtener la respuesta

    if 'items' in response:  # Verificar si hay elementos (videos) en la respuesta
        video_id = response['items'][0]['id']['videoId']  # Obtener el ID del primer video en los resultados
        video_url = f"https://www.youtube.com/watch?v={video_id}"  # Construir la URL del video de YouTube
        webbrowser.open(video_url)  # Abrir la URL del video en el navegador web predeterminado
    else:
        print("No se encontraron videos para la consulta:", consulta)  # Imprimir un mensaje si no se encontraron videos

#---------------------------------------------------- MAQUINA ESCUCHA Y HABLA ------------------------------------
salir = False 
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
        return salir #detener_programa() #manda una señal para que vaya a otra funcion a colocar un break 
       computadora_habla("Vamos a youtube a Buscar:" + texto_voz)
       print("Vamos a youtube a Buscar:  " + texto_voz)
       buscar_videos_youtube(texto_voz)  # Llamar a la función para buscar videos de YouTube del artista o banda proporcionado


 except:
      computadora_habla("Lo siento, no te he entendido")

def computadora_habla(frase): #Funcion para que la maquina hable segun lo que le pidamos
   comando_voz.say(str(frase))
   comando_voz.runAndWait() #se necesita para el cierre del comando de voz para que funcione


def inicializacion():
  while True:
   if salir == True:  #la variable salir dependendera de lo que pase con la funcion micriphone 
    computadora_habla("Has Activado el Comando Salir, Hasta pronto Mi bello Creador")
    break 
   else: 
     Microphone()  # Escuchar el comando de voz

inicializacion()















