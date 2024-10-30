import cv2
import numpy as np
import matplotlib.pyplot as plt
resim2=cv2.imread('kelebek.jpeg')
kusresmi=cv2.imread('kusresmi.jpg')
cv2.imshow('Kus resmi',kusresmi)
#maviden kırmızıdan ve yeşilden tonlar ayarlayacagız
print(kusresmi)#her bir pikselin matrissel değerini görmek için
print(kusresmi.shape)#kaç pikselden oluştugu yazıyor(genişlik yükseklik)
print(kusresmi.size)#boyutunu öğrenmek için
print(kusresmi.dtype)#hangi tipten veri kullanıldıgını görüyoruz

cv2.waitKey(0)
cv2.destroyAllWindows()
