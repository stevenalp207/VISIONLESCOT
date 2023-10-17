#librerias
import cv2
import os
from ultralytics import YOLO #libreria para lectura del modelo

import SeguimientoManos #Importar clase seguimiento manos
from SeguimientoManos import *

from tkinter import * #para interfaz
from PIL import Image, ImageTk #para interfaz
import imutils #para interfaz

# Funcion Visualizar
def detectormanos():
    # Leer modelo
    model = YOLO('VOCALESVn2.pt')
    # Detector
    detector = SeguimientoManos.detectormanos(Confdeteccion=0.90)

    while True:
        # Lectura captura
        ret, frame = cap.read()
        # extraer la info de la mano
        frame = detector.encontrarmanos(frame, dibujar=False)
        # Solo una mano
        lista1, bbox, mano = detector.encontrarposicion(frame, ManoNum=0, dibujarPuntos=False, dibujarBox=False,
                                                        color=[0, 255, 0])
        if mano == 1:
            xmin, ymin, xmax, ymax = bbox
            xmin = xmin - 40
            ymin = ymin - 40
            xmax = xmax + 40
            ymax = ymax + 40
            #recorte de la seña
            recorte = frame[ymin:ymax, xmin:xmax]

            # RESULTADOS
            resultados = model.predict(recorte, conf=0.50)
            if len(resultados) != 0:
                for results in resultados:
                    masks = results.masks
                    coordenadas = masks

                    anotaciones = resultados[0].plot()

            # mostrar recorte
            cv2.imshow("SENA", anotaciones)

        # mostrar fps
        cv2.imshow("LENGUAGE VOCALES", frame)
        # Leer teclado
        t = cv2.waitKey(1)
        if t == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# Funcion iniciar
def iniciar():
    global cap
    # Elegimos la camara
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    # cambiar resolucion
    cap.set(3, 1280)
    cap.set(4, 720)
    detectormanos() #Funcion mostrar camara

def paginaweb():
    import webbrowser
    webbrowser.open("https://lescot-web.com")
def instagram():
    import webbrowser
    webbrowser.open("https://www.instagram.com/visionlescot/")
def linkedin():
    import webbrowser
    webbrowser.open("https://www.linkedin.com/in/lesco-translator")
def video():
    global pantalla, frame, vid
    ret, frame = vid.read()
    if ret == True:
        frame = imutils.resize(frame, width=500, height=525)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)

        # Mostramos en el GUI
        lblVideo.configure(image=img)
        lblVideo.image = img
        lblVideo.after(10, video)
    else:
        update_video()
def update_video():
    global vid
    vid = cv2.VideoCapture('vocales.mp4')
    video()

# Variables
vid = None
cap = None

#  Ventana Principal
# Pantalla
pantalla = Tk() #root
pantalla.title("INTERFAZ | LESCOT | VISION ARTIFICIAL | MACHINE LEARNING")
pantalla.geometry("1280x720")  # Asignamos la dimension de la ventana
pantalla.attributes('-fullscreen', True)

# Fondo
imagenF = PhotoImage(file="Fondo.png")
background = Label(image = imagenF, text = "Fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Interfaz
#texto1 = Label(pantalla, text="VIDEO EN TIEMPO REAL: ")
#texto1.place(x = 580, y = 10)


# Botones
# Iniciar Video
imagenBI = PhotoImage(file="1.png")
inicio = Button(pantalla, text="Iniciar", image=imagenBI, height="80", width="400", command=iniciar)
inicio.place(x = 40, y = 200)

#Pagina web
imagenB1 = PhotoImage(file="2.png")
B1 = Button(pantalla, text="Web", image=imagenB1, height="80", width="400", command=paginaweb)
B1.place(x = 40, y = 320)

#Instagram
imagenB2 = PhotoImage(file="3.png")
B2 = Button(pantalla, text="IG", image=imagenB2, height="80", width="400", command=instagram)
B2.place(x = 40, y = 420)

#Linkedin
imagenB3 = PhotoImage(file="4.png")
B3 = Button(pantalla, text="IN", image=imagenB3, height="80", width="400", command=linkedin)
B3.place(x = 40, y = 520)

# Video
lblVideo = Label(pantalla)
lblVideo.place(x = 660, y = 120)

update_video() #iniciar video

pantalla.mainloop()
