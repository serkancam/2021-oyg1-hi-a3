import cv2
import numpy as np
import os

resim = np.zeros((400,400,3),dtype=np.uint8)

# ekranın tam ortasına 40 piksel yarıçapa sahip kenar rengi kırmızı ve kenar kalınlığı 2 piksel olan bir çember çiziniz
# Bu çemberi tam olarka içine alan, mavi kenrar rengi ve kenar kalınlığı 2 piksel olan bir kara çiziniz.

cv2.circle(resim,(200,200),40,(0,0,255),2)
cv2.rectangle(resim,(160,160),(240,240),(255,0,0),2)


cv2.imshow("resim",resim)
cv2.waitKey(0)

dosya_yolu=os.path.join(os.getcwd(),"images","chp1","calisma1.jpg")
cv2.imwrite(dosya_yolu,resim)