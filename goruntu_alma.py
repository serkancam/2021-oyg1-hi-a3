#goruntu_alma.py
import cv2
import numpy as np
import os 

# os komutu bize dosya yolunu oluşturmada yardımcı olacak
# os.getcwd() fonksiyonu çalıştığında içinde bulunduğu py dosyasının
# dizin yolunu verir.

cd = os.getcwd()
# print("**",cd,"**")
# marsrover.png resminin tam adresini(path) bulalım
# bunun için os.path.join işlemini kullancağız
dosya_yolu=os.path.join(cd,"images","chp1","marsrover.png")
# print("**",dosya_yolu,"**")

#resmi resim değişkenine değerlerini aktardık
resim=cv2.imread(dosya_yolu)

print("resim boyutu",resim.ndim)
print("resim shape",resim.shape)
print("resim yükseklik",resim.shape[0])
print("resim genişlik",resim.shape[1])
print("resim renk kanal sayısı",resim.shape[2])
# bir reim parçası alalaım
parca=resim[100:250,100:300]
parca1=resim[0:200,0:320]
parca2=resim[0:200,320:640]
parca3=resim[200:400,0:320]
parca4=resim[200:400,320:640]
# resme bir kare ekleyelim
baslangic=(100,70)
bitis=(350,380)
renk=(0,255,0)
kalinlik=4
cv2.rectangle(resim,baslangic,bitis,renk,kalinlik)
cv2.circle(resim,baslangic,30,(0,255,255),2)

cv2.imshow("resim",resim)
cv2.imshow("resmin parcasi",parca)
cv2.imshow("resmin parcasi1",parca1)
cv2.imshow("resmin parcasi2",parca2)
cv2.imshow("resmin parcasi3",parca3)
cv2.imshow("resmin parcasi4",parca4)


cv2.waitKey(0)

