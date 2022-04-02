import cv2
import streamlit as st
from cvzone.FaceDetectionModule import FaceDetector

# Load your camera.
detector = FaceDetector()

st.title("Face Detection")
run = st.checkbox("Run")
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    img, bboxs = detector.findFaces(frame)
    # BGR (Blue, Green, Red) -> RGB (Red, Green, Blue)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(img)
else:
    st.write("Stopped")
