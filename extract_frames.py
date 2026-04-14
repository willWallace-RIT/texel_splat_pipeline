import cv2
import os

VIDEO_PATH = "input.mp4"
OUT_DIR = "frames"
FPS_STEP = 5

os.makedirs(OUT_DIR, exist_ok=True)

cap = cv2.VideoCapture(VIDEO_PATH)
fps = cap.get(cv2.CAP_PROP_FPS)
skip = int(fps // FPS_STEP)

frame_id = 0
saved = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_id % skip == 0:
        cv2.imwrite(f"{OUT_DIR}/frame_{saved:05d}.png", frame)
        saved += 1

    frame_id += 1

cap.release()
print("Frames extracted:", saved)
