# f = open("input14.txt", "r")
#
# def final_position(x, y, vx, vy, sx, sy, t):
#     return (x + vx * t) % sx, (y + vy * t) % sy
#
# sx, sy = 101, 103
# t = 100
# s00, s01, s10, s11 = (0,) * 4
# for line in f:
#     line_split = line.split()
#     p = line_split[0][2:].split(",")
#     position = (int(p[0]), int(p[1]))
#     v = line_split[1][2:].split(",")
#     velocity = (int(v[0]), int(v[1]))
#     x, y = final_position(position[0], position[1], velocity[0], velocity[1], sx, sy, t)
#     if x <= (sx - 1) / 2 - 1:
#         if y <= (sy - 1) / 2 - 1:
#             s00 += 1
#         elif y >= (sy + 1) / 2:
#             s01 += 1
#     elif x >= (sx + 1) / 2:
#         if y <= (sy - 1) / 2 - 1:
#             s10 += 1
#         elif y >= (sy + 1) / 2:
#             s11 += 1
#
# s = s00 * s01 * s10 * s11
# print(s)
import numpy as np
import matplotlib.pyplot as plt

f = open("input14.txt", "r")

def final_position(x, y, vx, vy, sx, sy, t):
    return (x + vx * t) % sx, (y + vy * t) % sy

sx, sy = 101, 103
positions = []
velocities = []
for line in f:
    line_split = line.split()
    p = line_split[0][2:].split(",")
    position = (int(p[0]), int(p[1]))
    v = line_split[1][2:].split(",")
    velocity = (int(v[0]), int(v[1]))
    positions.append(position)
    velocities.append(velocity)

t = 0
while list(set(positions)) != positions:
    t += 1
    grid = np.zeros((sx, sy))
    for i in range(len(positions)):
        positions[i] = final_position(positions[i][0], positions[i][1], velocities[i][0], velocities[i][1], sx, sy, 1)
        grid[positions[i][0], positions[i][1]] += 1
    if np.sum(grid[:] > 1) == 0:
        plt.imshow(grid)
        plt.show()
        print(t)





