import numpy as np

pt1 = np.array((1, 3))
pt2 = np.array((3, 3))
pt3 = np.array((4, 3))
pt4 = np.array((5, 3))
pt5 = np.array((1, 2))
pt6 = np.array((4, 2))
pt7 = np.array((1, 1))
pt8 = np.array((2, 1))
c1 = np.array((1, 1))
c2 = np.array((2, 1))

pts = [pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8]

for pt in pts:
    pts.append(pt)
    print(pts)
    break

for pt in pts:
    dist = np.sqrt(np.sum(np.square(pt - c1)))
    dist1 = np.sqrt(np.sum(np.square(pt - c2)))
    distanceHeu = [dist, dist1]
    print(distanceHeu)

    if dist < dist1:
        distanceHeu = dist
        distanceHeu = [dist]
        min = distanceHeu
        print("min", min)

    else:
        distanceHeu = dist1
        distanceHeu = [dist1]
        mini = distanceHeu
        print("mini", mini)

c1 = np.array((1, 2))
pts = [pts[0], pts[4], pts[6]]
for pt in pts:
    dist = np.sqrt(np.sum(np.square(pt - c1)))
    distanceHeu = [dist]
    print(distanceHeu)

c2 = np.array((3.6, 2.4))
pts = [pts[1], pts[2]]

for pt in pts:
    dist = np.sqrt(np.sum(np.square(pt - c2)))
    distanceHeu = [dist]
    print(distanceHeu)
