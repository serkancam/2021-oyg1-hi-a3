import cv2
import os

yol = os.path.join(os.getcwd(),"images","chp2","rice_1.jpg")

goruntu = cv2.imread(yol)#bgr
gri = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)#bgr den griye
bulanik = cv2.GaussianBlur(gri,(3,3),0)

# _,sb=cv2.threshold(bulanik,150,255,cv2.THRESH_BINARY)
# sb = cv2.adaptiveThreshold(bulanik,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,3,3)

canny=cv2.Canny(bulanik,40,140)

konturlar,_=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(goruntu,konturlar,-1,(0,0,255),1)

cv2.imshow("orijinal",goruntu)
# cv2.imshow("bulanik",bulanik)
# cv2.imshow("sb",sb)
# cv2.imshow("canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()