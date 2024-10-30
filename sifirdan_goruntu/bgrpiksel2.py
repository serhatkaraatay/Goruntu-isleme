import cv2
import numpy as np
#bir pikseli beyaza boyadık

joker=cv2.imread("joker.jpg")
joker[50,30]=[255,255,255]
#bir çizgi şeklinde beyaza boyuyoruz
for i in range(30,101):
    joker[50,i]=[255,255,255]
cv2.imshow("joker resmi",joker)
cv2.waitKey(0)
cv2.destroyAllWindows()