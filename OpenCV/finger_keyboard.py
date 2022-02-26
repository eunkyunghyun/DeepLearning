from cvzone.HandTrackingModule import HandDetector
import cv2
import time


class Button:
    def __init__(self, pos, text, size=[100, 100]):
        self.x, self.y = pos
        self.text = text
        self.w, self.h = size

    def draw(self, img, bgrR, bgrT):
        # Draw a common rectangle.
        cv2.rectangle(frame, (self.x, 25 + self.y), (self.x + self.w, 25 + self.y + self.h),
                      bgrR, cv2.FILLED)
        # Take down the coincident text into the screen.
        cv2.putText(frame, self.text, (self.x + 25, self.y + 100), cv2.FONT_HERSHEY_PLAIN,
                    4, bgrT, 4)
        return img


# Import the camera by a VideoCapture object
cap = cv2.VideoCapture(0)
cap.set(3, 3000)
cap.set(4, 3000)

# Minimum Detection Confidence Threshold
detector = HandDetector(detectionCon=0.8)

# Set up keyboard buttons
keys = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'],
        ["Backspace"]]
buttons = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        if key == "Backspace":
            buttons.append(Button([25 + 125 * j, 125 * i], key, size=[400, 100]))
        else:
            buttons.append(Button([25 + 125 * j, 125 * i], key))

fx, fy, l = 0, 0, 0
console = ""
index = 0

while True:
    # Load an image taken consistently
    success, frame = cap.read()
    # Flip the frame abstracted from the webcam
    frame = cv2.flip(frame, 1)
    # Look up the hands and its landmarks with it drawing them
    hands, frame = detector.findHands(frame)
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 landmark points
        bbox1 = hand1["bbox"]  # Bounding box information: x, y, w, h
        centerPoint1 = hand1["center"]  # Center of each hand: cx, cy
        handType1 = hand1["type"]  # Indicate whether your hand is left or right
        fingers1 = detector.fingersUp(hand1)
        l, _, _ = detector.findDistance(lmList1[8], lmList1[12], frame)
        fx, fy = lmList1[8][0], lmList1[8][1]
    # Draw these buttons on the screen
    cv2.rectangle(frame, (100, 600), (1200, 700), (255, 255, 255), cv2.FILLED)
    for button in buttons:
        if button.x <= fx <= button.x + button.w and \
                button.y <= fy <= button.y + button.h and l < 50:
            button.draw(frame, (255, 255, 255), (255, 255, 255))
            if button.text == "Backspace":
                if len(console) > 0:
                    console = console[:-1]
                index = 0
            else:
                console += button.text
                time.sleep(0.25)
        else:
            button.draw(frame, (0, 0, 0), (255, 255, 255))
    button = Button([100, 575], console)
    button.draw(frame, (255, 255, 255), (0, 0, 0))
    cv2.imshow("Image", frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
