#librerias
import cv2
import os
from ultralytics import YOLO

import SeguimientoManos
from SeguimientoManos import *
# Importar clase seguimiento manos

#interfaz
import tkinter as tk
from tkinter import ttk



#abrir video camara
nCam = 0
cap = cv2.VideoCapture(1)
#cambiar resolucion
cap.set(3, 1280)
cap.set(4, 720)

#Leer modelo
model = YOLO('VOCALESVn2.pt')

#Detector
detector = SeguimientoManos.detectormanos(Confdeteccion=0.90)

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

        #RESULTADOS
        resultados = model.predict(recorte, conf=0.50)
        if len(resultados) != 0:
            for results in resultados:
                masks = results.masks
                coordenadas = masks

                anotaciones = resultados[0].plot()

        #mostrar recorte
        cv2.imshow("SENA", anotaciones)

    #mostrar fps
    cv2.imshow("LENGUAGE VOCALES", frame)
    #Leer teclado
    t = cv2.waitKey(1)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()