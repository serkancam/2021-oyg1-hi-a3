# goruntu_dondurme.py
from multiprocessing.connection import wait
import cv2
import numpy as np
import os

resim_yolu=os.path.join(os.getcwd(),"images","chp2","zebrasmall.png")
resim=cv2.imread(resim_yolu)

#gerekli bilgiler alınıyor
h,w,c=resim.shape
merkez=(h//2,w//2) 
aci=-45 
olcek=1.0
while True:   
    # döndürme matrisi oluşturalım
    dondurme_matrisi=cv2.getRotationMatrix2D(merkez,aci,olcek)
    #dönmüş resim
    donmus_resim=cv2.warpAffine(resim,dondurme_matrisi,(w,h))
    cv2.imshow("donmus resim",donmus_resim)
    cv2.imshow("orijinal",resim)
    aci+=5
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()