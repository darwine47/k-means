import numpy as np


M = np.array([(11, 7, 4, 6, 6, 7, 4, 4, 3),
              (7, 15, 8, 8, 9, 6, 3, 3, 2),
              (4, 8, 13, 7, 7, 4, 2, 3, 2),
              (6, 8, 7, 15, 7, 6, 6, 8, 6),
              (6, 9, 7, 7, 12, 4, 3, 5, 4),
              (4, 3, 2, 6, 3, 6, 13, 10, 9),
              (4, 3, 3, 8, 5, 5, 10, 15, 11),
              (3, 2, 2, 6, 4, 5, 9, 11, 12)])
distance = np.ones((len(M),9))

for i in range(len(M)):
    for j in range(i):
        distance[i][j] = (M[i][i] + M[j][j] - 2*M[i][j]) /( M[i][i] + M[j][j])
print(distance)



