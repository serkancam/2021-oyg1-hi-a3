import cv2
import os

yol1=os.path.join(os.getcwd(),"images","chp2","nature.jpg")
yol2=os.path.join(os.getcwd(),"images","chp2","salt-pepper.jpg")
doga = cv2.imread(yol1)
beyin=cv2.imread(yol2)

#filtreler 
# mean (ortalama)filter
doga_b1=cv2.blur(doga,(17,17))
beyin_b1=cv2.blur(beyin,(7,7))
beyin_b2=cv2.medianBlur(beyin,5)
#gösterimler
cv2.imshow("doga",doga)
cv2.imshow("doga b1",doga_b1)
cv2.imshow("beyin",beyin)
cv2.imshow("beyin b1",beyin_b1)
cv2.imshow("beyin b2",beyin_b2)
cv2.waitKey(0)