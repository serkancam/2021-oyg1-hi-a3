import cv2
import numpy as np
import os

yol = os.path.join(os.getcwd(), "images", "yuz.jpg")
goruntu = cv2.imread(yol)
# gri renk uzayına dönüşüm
# herbir piksel r,g, ve b renk değerleri için 8 bit(1 byte) bilgi tutar
# fakat gri tonlama her piksel için sadece 1 byte veri tutar
# opencv bgr ile okur
gri = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
# siyah-beyaz dönüşümü bir eşik değeri ile olur
# örneğin eşik değeri 60 ise 60 ve ondan küçük olan pikseller siyah diğerleri beyaz

t, sb = cv2.threshold(gri, 95, 255, cv2.THRESH_BINARY)


# gösterimler
cv2.imshow("renkli", goruntu)
cv2.imshow("gri", gri)
cv2.imshow("siyah beyaz",sb)
cv2.waitKey(0)
cv2.destroyAllWindows()
