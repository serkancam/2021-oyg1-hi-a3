import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,goruntu=cap.read()
    sonuc=cv2.Canny(goruntu,40,140)

    cv2.imshow("sonuc",sonuc)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows() 