import cv2
import numpy as np
import glob

frames = sorted(glob.glob("frames/*.png"))
stack = []

for f in frames:
    img = cv2.imread(f)
    stack.append(img.astype(np.float32))

stack = np.array(stack)

# Median fusion baseline for static scene
static_scene = np.median(stack, axis=0).astype(np.uint8)

cv2.imwrite("static_scene.png", static_scene)
print("Static scene built")
