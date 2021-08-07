import cv2
import numpy as np
import os

class basicColor:
    def __init__(self, ruta):
        imagen = cv2.imread(ruta)               # Leer imagen
        self.img = imagen                       # guardar imagen en self de img
        
    def displayProperties(self):
        pixels = self.img.shape[0] * self.img.shape[1]      # calcular el numero de pixeles
        canales = self.img.shape[2]                         # extraer numeros de canales
        print('El número de pixeles es: {}'.format(pixels))
        print('El número de canales es: {}'.format(canales))
        
    def makeBW(self):                           # método de Otsu
        img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)   # pasar imagen a grises
        ret, Ibw_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # incuentra valor Ibw_otsu
        cv2.imshow("Imagen", Ibw_otsu)                           # mostrando imagen
        cv2.waitKey(0)
    
    def colorize(self,h): 
        img_hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)     # transformar espacio de color de RGB a HSV
        img_hsv[:,:,0] = h                  # asignar valor h 
        img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)      # transformar espacio de color negro a BGR de HSV
        cv2.imshow("Image", img_bgr)
        cv2.waitKey(0)
     
### Ejecucion 
print("Inserte la ruta de la imagen") 
ruta = input() 
print()
#C:/Users/User/Desktop/1.jpg
# basicColor
resul = basicColor(ruta)
resul.displayProperties()
print()

# OTSU equalization
resul.makeBW()
print()

# Colorise image from h input
print("Inserte valor h")
h = int(input())
if h >= 0 and h <=179:
    resul.colorize(h)
else: 
    print('El número h no es valido, debe estar entre 0 y 179: {}'.format(h))
    
