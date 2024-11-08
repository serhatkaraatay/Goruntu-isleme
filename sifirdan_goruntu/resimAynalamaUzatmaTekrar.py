import cv2
import numpy as np
resim=cv2.imread("kurt.jpg")
aynalanan_resim=cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT)
uzatilan_resim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
tekraredilen_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)
cerceve_resim=cv2.copyMakeBorder(resim,10,10,10,10,cv2.BORDER_CONSTANT,value=(120,100,50))#en son cerceve rengi belirlenir
cv2.imshow("Tekrarlanan",tekraredilen_resim)
cv2.imshow(" Aynalama",aynalanan_resim)
cv2.imshow(" Uzatilan",uzatilan_resim)
cv2.imshow(" Cerceve",cerceve_resim)


cv2.waitKey(0)
cv2.destroyAllWindows()
