from cvzone.FaceDetectionModule import FaceDetector
import cv2

# Load your camera.
cap = cv2.VideoCapture(0)

# A model associated with detecting faces.
# Adhere to the direction of "Input -> Model -> Output".
detector = FaceDetector()

while True:
    ret, frame = cap.read()
    frame, bboxs = detector.findFaces(frame)
    
    # If "bboxs" exists, draw a series of dots on the center outline.
    if bboxs:
        center = bboxs[0]["center"]
        cv2.circle(frame, center, 5, (255, 0, 255), cv2.FILLED)

    # Display an image extracted from continuous components.
    cv2.imshow("Image", frame)

    # Quit the program by clicking 'q'.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
