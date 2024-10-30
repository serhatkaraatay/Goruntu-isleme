import cv2
import numpy as np
cocuk_resmi=cv2.imread("23nisan.jpg")
print("Resim Özellikleri : " , cocuk_resmi.shape)
kesit=cocuk_resmi[50:400,250:550]#y,x koordinatları
cocuk_resmi[0:350,100:400]=kesit  #kesilen parçayı resimin bir bölgesine yapıştırma işlemi
#kesiti aldığımız pikseller ve yapıştırılan kısım uyuşmalı
cocuk_resmi[ : , : ,0]=255 #resmin mavi kısmını beyaz yapma(0. kanal blue olduğu için mavi kanala işlem gerçekleşti)
cocuk_resmi[400:500,300:350]=(50,200,150)#resmi belirlenen alanına renk uyguladık
cv2.imshow("Cocuklar : ",cocuk_resmi)
#cv2.imshow("Cocuklar",kesit)
cv2.waitKey(0)
cv2.destroyAllWindows()