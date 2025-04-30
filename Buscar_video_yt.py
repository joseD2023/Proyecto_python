import webbrowser  # Importar el módulo webbrowser para abrir el navegador
from googleapiclient.discovery import build  # Importar la función build del módulo discovery de la biblioteca googleapiclient

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

nombre_artista = input("Introduce el nombre del artista o banda: ")  # Solicitar al usuario que ingrese el nombre del artista o banda
buscar_videos_youtube(nombre_artista)  # Llamar a la función para buscar videos de YouTube del artista o banda proporcionado
