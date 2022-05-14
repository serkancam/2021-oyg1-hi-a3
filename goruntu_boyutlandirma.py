# goruntu_boyutlandirma.py
import cv2
from cv2 import resize
import numpy as np
import os
#resim yolu
resim_yolu=os.path.join(os.getcwd(),"images","chp2","zebra.png")
# resmi dosya yolundan okuyalım
resim = cv2.imread(resim_yolu)
#resim bilgilerini aldık
h,w,c=resim.shape
print(resim.shape)
#resi en/boy oranını belirledik
resim_orani=w/h
# yeni değerler
h_yeni=400
w_yeni=int(resim_orani*h_yeni)
yeni_boyut=(w_yeni,h_yeni)
r1_resim=cv2.resize(resim,yeni_boyut,interpolation=cv2.INTER_AREA)
# siz yapın bu resmi w=300 değerine küçültünüz
w_yeni2=300
h_yeni2=int(w_yeni2/resim_orani)
yeni_boyut2=(w_yeni2,h_yeni2)
r2_resim=cv2.resize(resim,yeni_boyut2,interpolation=cv2.INTER_AREA)

#resmi 400,300 boyutunda yapalım(fakat oran bozulur)
r3_resim=cv2.resize(resim,(400,300),interpolation=cv2.INTER_AREA)
#  en ve boy oranı ile yeniden boyutlandırma
r4_resim=cv2.resize(resim,dsize=None,fx=0.6,fy=0.6,interpolation=cv2.INTER_AREA)


#resmi göster
cv2.imshow("orijinal",resim)
cv2.imshow("r1",r1_resim)
cv2.imshow("r2",r2_resim)
cv2.imshow("r3",r3_resim)
cv2.imshow("r4",r4_resim)
# bir tuş tıklanana kadar bekle
cv2.waitKey(0)