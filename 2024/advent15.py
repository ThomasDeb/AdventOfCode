# import numpy as np
# import matplotlib.pyplot as plt
#
# f = open("input15.txt", "r")
#
# walls = []
# boxes = []
# x = 0
# for line in f:
#     line_strip = line.strip()
#     if "#" not in line_strip:
#         break
#     if x == 0:
#         ny = len(line_strip)
#     for yx in range(ny):
#         if line_strip[yx] == "#":
#             walls.append((x, yx))
#         elif line_strip[yx] == "O":
#             boxes.append((x, yx))
#         elif line_strip[yx] == "@":
#             (rx, ry) = (x, yx)
#     x += 1
#
# nx = x
#
# directions = []
# for line in f:
#     line_strip = line.strip()
#     for ch in line_strip:
#         if ch == "v":
#             directions.append((1, 0))
#         elif ch == "^":
#             directions.append((-1, 0))
#         elif ch == ">":
#             directions.append((0, 1))
#         elif ch == "<":
#             directions.append((0, -1))
#         else:
#             print("Problem")
#
# grid = np.zeros((nx, ny))
#
# for (x, y) in walls:
#     grid[x, y] = 2
#
# for (x, y) in boxes:
#     grid[x, y] = 1
#
# for (dx, dy) in directions:
#     can_move = False
#     s = 1
#     (next_x, next_y) = (rx + s * dx, ry + s * dy)
#     while grid[next_x, next_y] != 2:
#         if grid[next_x, next_y] == 0:
#             can_move = True
#             (next_empty_x, next_empty_y) = (next_x, next_y)
#             break
#         s += 1
#         (next_x, next_y) = (rx + s * dx, ry + s * dy)
#     if can_move:
#         rx += dx
#         ry += dy
#         if (next_empty_x, next_empty_y) != (rx, ry):
#             grid[rx, ry] = 0
#             grid[next_empty_x, next_empty_y] = 1
#
# plt.imshow(grid)
# plt.show()
#
# s = 0
# for x in range(nx):
#     for y in range(ny):
#         if grid[x, y] == 1:
#             s += 100 * x + y
# print(s)

import numpy as np
import matplotlib.pyplot as plt

f = open("input15.txt", "r")

walls = []
boxes = []
x = 0
for line in f:
    line_strip = line.strip()
    if "#" not in line_strip:
        break
    if x == 0:
        ny = len(line_strip)
    for y in range(ny):
        if line_strip[y] == "#":
            walls.append((x, y))
        elif line_strip[y] == "O":
            boxes.append((x, y))
        elif line_strip[y] == "@":
            (rx, ry) = (x, 2 * y)
    x += 1

nx = x

directions = []
for line in f:
    line_strip = line.strip()
    for ch in line_strip:
        if ch == "v":
            directions.append((1, 0))
        elif ch == "^":
            directions.append((-1, 0))
        elif ch == ">":
            directions.append((0, 1))
        elif ch == "<":
            directions.append((0, -1))
        else:
            print("Problem")

grid = np.zeros((nx, 2 * ny))

for (x, y) in walls:
    grid[x, 2 * y] = 2
    grid[x, 2 * y + 1] = 2

for (x, y) in boxes:
    grid[x, 2 * y] = -1
    grid[x, 2 * y + 1] = 1

grid[rx, ry] = 3
plt.imshow(grid)
plt.show()
grid[rx, ry] = 0

for (dx, dy) in directions:
    can_move = True
    check = [(rx + dx, ry + dy)]
    boxes_to_move = []
    while can_move and check:
        check_next = []
        for (x, y) in check:
            if grid[x, y] == 2:
                can_move = False
                break
            elif grid[x, y] == -1:
                boxes_to_move.append((x, y))
                if dx == 0:
                    if dy == 1:
                        check_next.append((x + dx, y + 1 + dy))
                    else:
                        check_next.append((x + dx, y + dy))
                else:
                    check_next.append((x + dx, y + dy))
                    check_next.append((x + dx, y + 1 + dy))
            elif grid[x, y] == 1:
                boxes_to_move.append((x, y - 1))
                if dx == 0:
                    if dy == 1:
                        check_next.append((x + dx, y + dy))
                    else:
                        check_next.append((x + dx, y - 1 + dy))
                else:
                    check_next.append((x + dx, y + dy))
                    check_next.append((x + dx, y - 1 + dy))
        check = check_next
    if can_move:
        rx += dx
        ry += dy
        boxes_to_move.reverse()
        for (x, y) in boxes_to_move:
            grid[x, y] = 0
            grid[x, y + 1] = 0
            grid[x + dx, y + dy] = -1
            grid[x + dx, y + 1 + dy] = 1

grid[rx, ry] = 3
plt.imshow(grid)
plt.show()
grid[rx, ry] = 0

s = 0
for x in range(nx):
    for y in range(2 * ny):
        if grid[x, y] == -1:
            s += 100 * x + y
print(s)
