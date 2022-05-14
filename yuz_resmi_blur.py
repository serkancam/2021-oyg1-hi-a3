import cv2
import numpy as np
import os

yol=os.path.join(os.getcwd(),"images","yuz.jpg")
goruntu=cv2.imread(yol)
goruntu=cv2.blur(goruntu,(35,35))

cv2.imshow("sonuc",goruntu)

cv2.waitKey(0)
cv2.destroyAllWindows()