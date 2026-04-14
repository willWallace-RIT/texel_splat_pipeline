import cv2
import numpy as np
import glob

frames = sorted(glob.glob("frames/*.png"))

points = []
colors = []

for f in frames:
    img = cv2.imread(f)
    h, w, _ = img.shape

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # naive sampling of "geometry points"
    step = 10
    for y in range(0, h, step):
        for x in range(0, w, step):
            z = gray[y, x] / 255.0
            points.append([x, y, z])
            colors.append(img[y, x] / 255.0)

np.save("points.npy", np.array(points))
np.save("colors.npy", np.array(colors))

print("Point cloud generated")
