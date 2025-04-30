import tkinter as tk
from pytube import YouTube
from tkinter import messagebox as ms
from tkinter import *
from tkinter import filedialog
import threading
#seleccionar un directorio en donde ira la descarga
def seleccionar_directorio():
    directorio_descarga = filedialog.askdirectory()
    ms.showinfo("Directorio Seleccionado", f"Directorio de descarga: {directorio_descarga}")
    return directorio_descarga

#Descargar en mp3 codigo 
def descargar_audio():
    def descargar():
        try:
            url = entrada_url.get()
            directorio_descarga = seleccionar_directorio()

            if directorio_descarga:
                video = YouTube(url)
                stream_audio = video.streams.filter(only_audio=True).first()
                stream_audio.download(output_path=directorio_descarga, filename=f"{video.title}.mp3")
                ms.showinfo("Éxito", "Descarga completada de audio en formato MP3")
            else:
                ms.showinfo("Cancelado", "Descarga de audio cancelada. No se seleccionó un directorio.")
        except Exception as e:
            ms.showerror("Error", f"Hubo un error: {str(e)}")

    threading.Thread(target=descargar).start()

#Vamos a crear un codiog para borrar el texto que pongamos en el entry
def borrar_texto():
 entrada_url.delete(0, tk.END)
#CODIGO PARA DESCARGAR VIDEO A TRAVES D PYTUBE 
def descargar_video():
    def descargar():
        try:
            link = entrada_url.get()
            directorio_descarga = seleccionar_directorio()

            if directorio_descarga:
                yt = YouTube(link)
                stream = yt.streams.get_highest_resolution()
                stream.download(output_path=directorio_descarga)
                ms.showinfo("Éxito", "Descarga completada")
            else:
                ms.showinfo("Cancelado", "Descarga de video cancelada. No se seleccionó un directorio.")
        except Exception as e:
            ms.showerror("Error", f"Hubo un error: {str(e)}")

    threading.Thread(target=descargar).start()

ventana = tk.Tk()
ventana.geometry("900x700")
ventana.config(background="#008B8B")
ventana.title("Descargador SpotySe")
#creamos el boton el cual va a descargar el video 

btn_descargar = tk.Button(ventana, text="Descargar video", bg="#001F3F", fg="white", width=25, command=descargar_video)
btn_descargar.place(x=480, y=80, height=30)

#Vamos a crear un boton para descargar en mp3
btn_mp3 = tk.Button(ventana, text="Descargar Audio", bg="#001F3F", fg="white", width=25, command=descargar_audio)
btn_mp3.place(x=480, y=120, height=30)


#La entrada de la url para descargarlo
entrada_url = tk.Entry(ventana)
entrada_url.place(x=150, y=80, width=290, height=30)

#creamos un label para anunciar para que sirve 
label_instrucciones = tk.Label(ventana, text="Descargador de videos Online Gratis", bg="#008B8B", fg="white", font=("Helvetica", 16, "bold"))
label_instrucciones.place(x=230, y=40)
#crearemos una nota con label para ver como funciona nuestro programa
label_nota = tk.Label(ventana, text="Instrucciones: \n 1. Ingresa la URL del video de YouTube.\n  2. Haz clic en Descargar Video.\n 3. Espera a que se complete la descarga. \n ¡Disfruta de tus videos descargados!", bg="#008B8B", fg="white")
label_nota.place(x=150, y=130)
#vamos a crear un boton salir 

def salir_programa():
 ventana.quit()

boton_salir = tk.Button(ventana, text="Salir", bg="#001F3F", fg="white", width=25, command=salir_programa)
boton_salir.place(x=690, y=300)
#Vamos a crear un boton para borrar el texto en el widget entry

btn_borrar = tk.Button(ventana, text="Borrar Texto", bg="black", fg="white", command=borrar_texto)
btn_borrar.place(x=150, y=300)

#Crearemos nuestro frame de abajo 
frame1 = tk.Frame(ventana, bg="white", width=10000)
frame1.place(x=0, y=400, height=500)
#----------------------------------------------------------------------
#AHORA TRABAJAREMOS EN NUESTRO FRAME 
label_frame = tk.Label(frame1, text="Download es compatible con diferentes \n webs como:", bg="white", fg="black", font=("Helvetica", 16, "bold"))
label_frame.place(x=230, y=40)

#vamos agregar una imagen a mi frame

imagen = PhotoImage(file="E:/Curso Youtube python/logo.png")
etiqueta_imagen = tk.Label(frame1, image=imagen)
etiqueta_imagen.place(x=0, y=60)
ventana.mainloop()









