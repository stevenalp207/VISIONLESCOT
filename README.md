# VISIONLESCOT 🤝
***RESUMEN***— LESCOT es un proyecto realizado para la feria de Ciencia y Tecnología EXPOTEC 2023 en el CTP Cedes Don Bosco. Proyecto LESCOT es realizado por 4 estudiantes de la Gen. 2025 (Décimo año) de la especialidad en Electrónica Industrial, que buscan proponer una solución a las brechas de comunicación existentes en la vida cotidiana entre las personas oyentes y sordas, con la adaptabilidad de un traductor de LESCO, solución que se espera que sea utilizada por la comunidad costarricense. 

***ABSTRACT***— LESCOT is a project created for the Science and Technology Expo EXPOTEC 2023 at CTP Cedes Don Bosco. Project LESCOT is undertaken by 4 students from the 2025 GEN (Tenth Grade) specializing in Industrial Electronics. They aim to provide a solution to the existing communication gaps in daily life between hearing and deaf individuals, with the adaptability of a LESCO translator, a solution intended for use by the Costa Rican community.

![Logo de CEDES para otros fondos](https://github.com/stevenalp207/VISIONLESCOT/assets/144076399/6e273c75-4a27-4ef7-91cb-c001d77da450)
![LESCOT2](https://github.com/stevenalp207/VISIONLESCOT/assets/144076399/113b04e3-d4af-455a-9041-383a45825a9f)

## NUESTRO OBJETIVO
- Proponer una solución a las brechas de comunicación en familias o la propia vida cotidiana de las personas con discapacidad auditiva con la adaptabilidad de un “traductor” de LESCO (Lenguaje de Señas Costarricense) a texto en pantalla, mejorando así la inclusión y accesibilidad a la información y servicios para la comunidad costarricense.

------------

## PROCEDIMIENTO DEL PROGRAMA
El programa "data", consta de dos procesos, el primero, se realiza la detección precisa de las manos, con esto también un proceso automatizado de captura y almacenamiento de imágenes en una carpeta, las cuales son las señas que vamos a utilizar para la segmentación  Con las imágenes se pasa a un proceso llamado segmentación de instancias, donde se crean bases de datos con patrones de las imágenes capturadas, debido a que esto será parte de lo que la computadora va a aprender en el proceso de Machine Learning (ya antes explicado) con YOLOV8.

------------


El Machine Learning culmina con la creación de un modelo con toda la información adquirida durante el proceso de entrenamiento y se logra pasar al segundo programa llamado "inferencia". Este programa se encarga de dos tareas esenciales, en primer lugar, realiza una detección precisa de manos en un video y lectura del modelo, esta detección es de suma importancia para identificar las coordenadas y forma de la mano. Una vez el programa es ejecutado y la información de la mano es extraída, se realizan diferentes comparaciones con la información obtenida en el modelo para realizar un sistema de predicciones. Cuando se encuentra una coincidencia entre la información de la mano y el modelo, se resalta un contorno de color con la forma de la mano detectada haciendo representación a alguna de las vocales dentro del modelo

## DIAGRAMA DE FLUJOS
***PROGRAMA 'DATA'***

------------

![graph datapy](https://github.com/stevenalp207/VISIONLESCOT/assets/144076399/05932f0c-ab56-4a52-ba83-5afc3cf7f3f6)

------------

***PROGRAMA 'INFERENCIA'***

------------

![graph inferenciapy](https://github.com/stevenalp207/VISIONLESCOT/assets/144076399/d7aeae40-22c9-4365-b78b-5c055b3501f7)

------------


## USO DEL PROGRAMA
Una vez el programa es ejecutado, se debe de poner una única mano en la cámara, con esto se iniciará el proceso antes dicho de predicciones y se comenzará a mostrar en pantalla la vocal que se está realizando.

## ERRORES DEL PROGRAMA
- 1)	Al colocar la mano en pantalla se deberá esperar algunos segundos a que el programa realice la primera predicción.

------------

- 2)	Si se colocan dos manos en pantalla, el programa puede llegar a confundirse y no saber cuál de las dos manos deberá detectar, esto podría causar un cierre del programa.

------------

- 3)	Recordar que es un sistema de predicciones y podrán existir excepciones donde la confianza de detección de la vocal no sea la esperada.

------------

- 4)	Si el programa realiza el sistema de predicciones y no encuentra ningún coincidente y la mano sigue en pantalla, se puede llegar a causar un cierre del programa.

------------

# NUESTRA PAGINA WEB
> Puedes visitarnos y saber de nuestro proyecto en nuestra página web oficial: https://lescot-web.com
------------
> You can visit and learn about our project in our official web page: https://en.lescot-web.com

## YOLOV8n args
| TASK | MODE | EPOCHS | MODEL | IMGSZ | BATCH |
| ------------ | ----------- | ----------- | ------------ | ----------- | ----------- |
| SEGMENT | TRAIN | 40 | YOLOV8N-SEGMENT | 640 | 2 |

##  COLORES LABELS VOCALES
| A | E | I | O | U |
| ------------ | ----------- | ----------- | ------------ | ----------- |
| AMARILLO | VERDE | ROJO | ROSADO | NARANJA |
