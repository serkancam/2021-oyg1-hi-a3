from tkinter.tix import Tree
import cv2

cap = cv2.VideoCapture(0)

while True:
    durum,goruntu=cap.read()
    gri=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    t,sb=cv2.threshold(gri,70,255,cv2.THRESH_BINARY)
    kenarlar=cv2.Canny(gri,80,170)
    cv2.imshow("kamera",goruntu)
    cv2.imshow("kenarlar",kenarlar)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()