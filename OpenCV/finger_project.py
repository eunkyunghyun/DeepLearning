from cvzone.HandTrackingModule import HandDetector
import cv2

# Import the camera by a VideoCapture object
cap = cv2.VideoCapture(0)

# Minimum Detection Confidence Threshold
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

cx, cy, w, h = 100, 100, 200, 200

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
        l, _, _ = detector.findDistance(lmList1[8], lmList1[12], frame)
        if l < 50:
            if cx - w // 2 < bbox1[0] < cx + w // 2 and cy - h // 2 < bbox1[1] < cx + h // 2:
                colorR = (0, 255, 0)
                cx, cy = bbox1[0], bbox1[1]
        else:
            colorR = (255, 0, 255)
    cv2.rectangle(frame, (cx - w // 2, cy - h // 2), (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)
    cv2.imshow("Image", frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
