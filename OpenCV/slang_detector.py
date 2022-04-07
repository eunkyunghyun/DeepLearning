from cvzone.HandTrackingModule import HandDetector
from playsound import playsound
import cv2

# Import the camera by a VideoCapture object
cap = cv2.VideoCapture(0)

# Minimum Detection Confidence Threshold
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

cx, cy, w, h = 100, 100, 200, 200
count = 100

while True:
    # Load an image taken consistently
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # Discover the hands and its landmarks
    hands, frame = detector.findHands(frame)
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 landmark points
        bbox1 = hand1["bbox"]  # Bounding box information: x, y, w, h
        centerPoint1 = hand1["center"]  # Center of the hand: cx, cy
        handType1 = hand1["type"]  # Indicate whether your hand is left or right
        fingers1 = detector.fingersUp(hand1)
        target = fingers1.pop(2)
        if count >= 100:
            count = 10
        if target == 1 and any(fingers1) == 0 and count >= 10:
            print("A slang expression is detected!")
            playsound("./resource/caution.mp3")
            count = 0
        count += 1
    cv2.rectangle(frame, (cx - w // 2, cy - h // 2), (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)
    cv2.imshow("Image", frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
