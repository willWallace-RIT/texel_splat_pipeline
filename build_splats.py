import numpy as np

points = np.load("points.npy")
colors = np.load("colors.npy")

splats = []

for p, c in zip(points, colors):
    splats.append({
        "position": p.tolist(),
        "color": c.tolist(),
        "opacity": 0.6,
        "covariance": [1.0, 0.0, 1.0]
    })

np.save("splats.npy", np.array(splats, dtype=object))
print("Splats built")
