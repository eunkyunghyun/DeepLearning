from cvzone.HandTrackingModule import HandDetector
import cv2

# Bring the camera by VideoCapture object
cap = cv2.VideoCapture(0)

while True:
    # Load an image taken consistently
    success, frame = cap.read()
    cv2.imshow("Image", frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
