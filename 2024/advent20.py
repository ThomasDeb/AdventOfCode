# import numpy as np
# import matplotlib.pyplot as plt
#
# f = open("input20.txt", "r")
# costs = []
# i = 0
# for line in f:
#     line_strip = line.strip()
#     if i == 0:
#         nj = len(line_strip)
#     l = [-1 if s == "#" else 0 for s in line_strip]
#     nj = len(l)
#     costs.append(l)
#     if "S" in line_strip:
#         j = line_strip.index("S")
#         start = (i, j)
#     if "E" in line_strip:
#         j = line_strip.index("E")
#         end = (i, j)
#     i += 1
# ni = i
#
# distances = np.zeros((ni, nj))
# for i in range(ni):
#     distances[i, :] = costs[i]
#
# possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# def idx_in_range(i, j):
#     if i >= 0 and i < ni and j >= 0 and j < nj:
#         return True
#     else:
#         return False
#
# coordinates = [end]
# while coordinates:
#     next_coordinates = []
#     for idx in range(len(coordinates)):
#         i, j = coordinates[idx]
#         for (di, dj) in possible_directions:
#             if idx_in_range(i + di, j + dj):
#                 if distances[i + di, j + dj] == 0 or (distances[i + di, j + dj] > distances[i, j] + 1):
#                     distances[i + di, j + dj] = distances[i, j] + 1
#                     next_coordinates.append((i + di, j + dj))
#
#     next_coordinates = list(set(next_coordinates))
#     coordinates = next_coordinates
#
# plt.imshow(distances)
# plt.colorbar()
# plt.show()
#
# coordinates = [start]
# cheats = []
# time_save = 100
# while coordinates:
#     next_coordinates = []
#     for idx in range(len(coordinates)):
#         i, j = coordinates[idx]
#         for (di, dj) in possible_directions:
#             if idx_in_range(i + di, j + dj):
#                 if distances[i + di, j + dj] == -1:
#                     for (dii, djj) in possible_directions:
#                             if idx_in_range(i + di + dii, j + dj + djj):
#                                 if (d:= distances[i + di + dii, j + dj + djj]) >=0 and d <= distances[i, j] - time_save - 2:
#                                     cheats.append((i + di, j + dj, i + di + dii, j + dj + djj))
#                 else:
#                     if distances[i + di, j + dj] == distances[i, j] - 1:
#                         next_coordinates.append((i + di, j + dj))
#     next_coordinates = list(set(next_coordinates))
#     coordinates = next_coordinates
#
# cheats = list(set(cheats))
# print(len(cheats))

import numpy as np
import matplotlib.pyplot as plt

f = open("input20.txt", "r")
costs = []
i = 0
for line in f:
    line_strip = line.strip()
    if i == 0:
        nj = len(line_strip)
    l = [-1 if s == "#" else -2 for s in line_strip]
    nj = len(l)
    costs.append(l)
    if "S" in line_strip:
        j = line_strip.index("S")
        start = (i, j)
    if "E" in line_strip:
        j = line_strip.index("E")
        end = (i, j)
    i += 1
ni = i

distances = np.zeros((ni, nj))
for i in range(ni):
    distances[i, :] = costs[i]
distances[end[0], end[1]] = 0

possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def idx_in_range(i, j):
    if i >= 0 and i < ni and j >= 0 and j < nj:
        return True
    else:
        return False

coordinates = [end]
while coordinates:
    next_coordinates = []
    for idx in range(len(coordinates)):
        i, j = coordinates[idx]
        for (di, dj) in possible_directions:
            if idx_in_range(i + di, j + dj):
                if distances[i + di, j + dj] == -2 or (distances[i + di, j + dj] > distances[i, j] + 1):
                    distances[i + di, j + dj] = distances[i, j] + 1
                    next_coordinates.append((i + di, j + dj))

    next_coordinates = list(set(next_coordinates))
    coordinates = next_coordinates

plt.imshow(distances)
plt.colorbar()
plt.show()

coordinates = [start]
cheats = []
time_save = 100
len_cheat = 20
while coordinates:
    next_coordinates = []
    for idx in range(len(coordinates)):
        i, j = coordinates[idx]
        for n in range(1, len_cheat + 1):
            for m in range(n + 1):
                for si in [-1, 1]:
                    for sj in [-1, 1]:
                        dii, djj = m * si, (n - m) * sj
                        if idx_in_range(i + dii, j + djj):
                            if (d := distances[i + dii, j + djj]) >= 0 and d <= distances[i, j] - time_save - n:
                                # if distances[i, j] - d - n - 1 == 74:
                                cheats.append((i, j, i + dii, j + djj))
        for (di, dj) in possible_directions:
            if idx_in_range(i + di, j + dj):
                if distances[i + di, j + dj] != -1 and (distances[i + di, j + dj] == distances[i, j] - 1):
                        next_coordinates.append((i + di, j + dj))
    next_coordinates = list(set(next_coordinates))
    coordinates = next_coordinates

cheats = list(set(cheats))
print(len(cheats))

