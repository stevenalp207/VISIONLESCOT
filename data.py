#importar librerias
import cv2
import os
#interfaz

import SeguimientoManos
from SeguimientoManos import *
# Importar clase seguimiento manos

#Carpeta informacion
nombre = 'Letra_PRUEBA2'
direccion = 'C:/Users/salpi/OneDrive/Escritorio/VOCALESV2/data'
carpeta = direccion + '/' + nombre

#si no existe, se crea
if not os.path.exists(carpeta):
    print("CARPETA CREADA", carpeta)
    os.makedirs(carpeta)

    #abrir video camara
nCam = 0
url1 = "http://192.168.32.104:4747/video"
cap = cv2.VideoCapture(nCam)
#cambiar resolucion
cap.set(3, 1280)
cap.set(4, 720)

#contador
cont = 0
#Detector
detector = SeguimientoManos.detectormanos(Confdeteccion=0.9)
while True:
    #Lectura captura
    ret, frame = cap.read()
    #extraer la info de la mano
    frame = detector.encontrarmanos(frame, dibujar=False)
    #Solo una mano
    lista1, bbox, mano = detector.encontrarposicion(frame, ManoNum=0, dibujarPuntos=False, dibujarBox=False, color=[0,255,0])
    if mano == 1:
        xmin, ymin, xmax, ymax =  bbox
        xmin = xmin - 40
        ymin = ymin - 40
        xmax = xmax + 40
        ymax = ymax + 40
        #recorte para ver la imagen a guardar
        recorte = frame[ymin:ymax, xmin:xmax]

        #Redimensionar
        #recorte = cv2.resize(recorte, (640, 640), interpolation=cv2.INTER_CUBIC)

        #almacenar imagenes
        cv2.imwrite(carpeta + "/PRUEBA_{}.jpg".format(cont), recorte)
        #aumentar contador
        cont = cont + 1
        #mostrar recorte
        cv2.imshow("RECORTE", recorte)

    #mostrar fps
    cv2.imshow("LENGUAGE VOCALES", frame)
    #Leer teclado
    t = cv2.waitKey(1)
    if t == 27 or cont == 100:
        break

cap.release()
cv2.destroyAllWindows()
