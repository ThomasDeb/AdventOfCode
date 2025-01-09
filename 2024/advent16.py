# import numpy as np
# import matplotlib.pyplot as plt
#
# def cost_change_directions(d1, d2):
#     p = d1[0] * d2[0] + d1[1] * d2[1]
#     if p == 1:
#         return 0
#     elif p == 0:
#         return 1000
#     elif p == -1:
#         return 2000
#
#
# f = open("input16.txt", "r")
# costs = []
# i = 0
# for line in f:
#     line_strip = line.strip()
#     if i == 0:
#         nj = len(line_strip)
#     l = [0 if s == "#" else 1 for s in line_strip]
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
# labyrinth = np.zeros((ni, nj))
# for i in range(ni):
#     labyrinth[i, :] = costs[i]
#
#
# direction_costs = [l.copy() for l in costs]
# possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# def idx_in_range(i, j):
#     if i >= 0 and i < ni and j >= 0 and j < nj:
#         return True
#     else:
#         return False
#
# coordinates = [start]
# directions = [(0, 1)]
# costs[start[0]][start[1]] = [0]
# direction_costs[start[0]][start[1]] = [(0, 1)]
# while coordinates:
#     next_coordinates = []
#     for idx in range(len(coordinates)):
#         i, j = coordinates[idx]
#         for (di, dj) in possible_directions:
#             if idx_in_range(i + di, j + dj) and costs[i + di][j + dj] != 0:
#                 l = [c + cost_change_directions(d, (di, dj)) + 1 for c, d in zip(costs[i][j], direction_costs[i][j])]
#                 min_idx = np.argmin(l)
#                 if costs[i + di][j + dj] != 1:
#                     for k in range(len(costs[i + di][j + dj])):
#                         new_cost = l[min_idx] + cost_change_directions((di, dj), direction_costs[i + di][j + dj][k])
#                         if new_cost < costs[i + di][j + dj][k]:
#                             costs[i + di][j + dj][k] = new_cost
#                             next_coordinates.append((i + di, j + dj))
#                 else:
#                     next_coordinates.append((i + di, j + dj))
#                     costs[i + di][j + dj] = []
#                     direction_costs[i + di][j + dj] = []
#                     for dd in possible_directions:
#                         costs[i + di][j + dj].append(l[min_idx] + cost_change_directions((di, dj), dd))
#                         direction_costs[i + di][j + dj].append(dd)
#
#     next_coordinates = list(set(next_coordinates))
#     coordinates = next_coordinates
#
#     # im_cost = np.zeros((ni, nj))
#     # for i in range(ni):
#     #     for j in range(nj):
#     #         if type(costs[i][j]) == list:
#     #             im_cost[i, j] = min(costs[i][j])
#     # plt.imshow(im_cost)
#     # plt.colorbar()
#     # plt.show()
#     # pass
#
# print(min(costs[end[0]][end[1]]))

import numpy as np
import matplotlib.pyplot as plt

def cost_change_directions(d1, d2):
    p = d1[0] * d2[0] + d1[1] * d2[1]
    if p == 1:
        return 0
    elif p == 0:
        return 1000
    elif p == -1:
        return 2000


f = open("input16.txt", "r")
costs = []
i = 0
for line in f:
    line_strip = line.strip()
    if i == 0:
        nj = len(line_strip)
    l = [0 if s == "#" else 1 for s in line_strip]
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

labyrinth = np.zeros((ni, nj))
for i in range(ni):
    labyrinth[i, :] = costs[i]


direction_costs = [l.copy() for l in costs]
possible_directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def idx_in_range(i, j):
    if i >= 0 and i < ni and j >= 0 and j < nj:
        return True
    else:
        return False

coordinates = [start]
directions = [(0, 1)]
costs[start[0]][start[1]] = [1000, 2000, 0, 1000]
direction_costs[start[0]][start[1]] = possible_directions
while coordinates:
    next_coordinates = []
    for idx in range(len(coordinates)):
        i, j = coordinates[idx]
        for (di, dj) in possible_directions:
            if idx_in_range(i + di, j + dj) and costs[i + di][j + dj] != 0:
                l = [c + cost_change_directions(d, (di, dj)) + 1 for c, d in zip(costs[i][j], direction_costs[i][j])]
                min_idx = np.argmin(l)
                if costs[i + di][j + dj] != 1:
                    for k in range(len(costs[i + di][j + dj])):
                        new_cost = l[min_idx] + cost_change_directions((di, dj), direction_costs[i + di][j + dj][k])
                        if new_cost < costs[i + di][j + dj][k]:
                            costs[i + di][j + dj][k] = new_cost
                            next_coordinates.append((i + di, j + dj))
                else:
                    next_coordinates.append((i + di, j + dj))
                    costs[i + di][j + dj] = []
                    direction_costs[i + di][j + dj] = []
                    for dd in possible_directions:
                        costs[i + di][j + dj].append(l[min_idx] + cost_change_directions((di, dj), dd))
                        direction_costs[i + di][j + dj].append(dd)

    next_coordinates = list(set(next_coordinates))
    coordinates = next_coordinates

coordinates = [end]
directions_idx = [np.argmin(costs[end[0]][end[1]])]
paths = [end]
while coordinates:
    next_coordinates = []
    next_direction_idx = []
    for idx in range(len(coordinates)):
        i, j = coordinates[idx]
        if i == 7 and j == 5:
            pass
        for k in range(len(possible_directions)):
            di, dj = possible_directions[k]
            if idx_in_range(i + di, j + dj) and costs[i + di][j + dj] != 0:
                cost_temp = costs[i + di][j + dj][-k - 1] + cost_change_directions(possible_directions[directions_idx[idx]], (-di, -dj)) + 1
                if cost_temp == costs[i][j][directions_idx[idx]]:
                    next_coordinates.append((i + di, j + dj))
                    next_direction_idx.append(possible_directions.index((-di, -dj)))
    paths.extend(next_coordinates)
    coordinates = next_coordinates
    directions_idx = next_direction_idx

print(len(set(paths)))

im_cost = np.zeros((ni, nj))
for i in range(ni):
    for j in range(nj):
        if type(costs[i][j]) == list:
            im_cost[i, j] = 1
        if (i, j) in paths:
            im_cost[i, j] = 2
plt.imshow(im_cost)
plt.colorbar()
plt.show()
