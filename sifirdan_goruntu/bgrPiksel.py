import cv2
import numpy as np
kurtResmi=cv2.imread("kurt.jpg")
cv2.imshow("Kurt Resmi",kurtResmi)
print(kurtResmi[(230,80)])#230 aşağıya 80 saga (blue green red şeklinde)
print("resim boyutu : "+str(kurtResmi.size))
print("Resmin Özellikleri : "+str(kurtResmi.shape))
print("Resmin veri tipi : "+str(kurtResmi.dtype))
cv2.waitKey(0)
cv2.destroyAllWindows()