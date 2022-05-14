import cv2


kamera = cv2.VideoCapture(0)  # linux ta 0 veya -1, windowsta 0
# VideoCapture ile kayıtlı bir video da alınabilirdi.

while True:
    durum, goruntu = kamera.read()
    goruntu=cv2.flip(goruntu,1)
    cv2.imshow("kamera", goruntu)
    if cv2.waitKey(1) & 0xFF == ord("q"):#cv2.waitKey(20) == 113:
        break

kamera.release()
cv2.destroyAllWindows()
