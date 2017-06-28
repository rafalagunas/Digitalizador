#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import call
import os

host = "192.168.0.103:8080" #Dirección ip del dispositivo móvil con cámara
if len(sys.argv)>1:
    host = sys.argv[1]

print 'Streaming ' + hoststr #Mostramos la ip desde donde se hace el streaming

bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow(hoststr,i)


        if cv2.waitKey(1) & 0xFF == ord('s'): #El programa espera a que el usuario presione la tecla S
	   os.mkdir("formatos")
           cv2.imwrite( "formatos/imagen.jpg", i ) #Cuando la tecla es presionada, se escribe la pantalla en el archivo imagen.jpg
           #cv2.destroyWindow(hoststr)
           asString = pytesseract.image_to_string(Image.open('formatos/imagen.jpg'),lang='spa') #Convertimos la imagen a una cadena de texto
           print asString #Imprimimos la cadena
           break
text_file = open("formatos/Texto.txt", "w") #Creamos el archivo de texto para editarlo
text_file.write("%s" %asString) #Añadimos la cadena de texto resultante en la función anterior
text_file.close() #Se cierra el archivo y se guarda

#! /bin/bash
#script

#os.system("espeak -v es-la -s110 -p135 -f formatos/Texto.txt -w formatos/audio.mp3") # s representa las palabras leídas por minuto, p el pitch
#os.system("cat formatos/Texto.txt | iconv -c -f utf-8 -t ISO-8859-1 | enscript -o formatos/file.ps") #Codificar el archivo txt en UTF-8, conversión a postscript
#os.system("ps2pdf formatos/file.ps formatos/file.pdf") #Conversión de postscript a pdf
#os.system("rm formatos/file.ps") #Se elimina el archivo postscript innecesario
#os.system("ebook-convert formatos/file.pdf formatos/file.epub --title título --authors autores") #Creación del formato epub mediante el pdf
os.system("clear") #Limpiamos la pantallahola
