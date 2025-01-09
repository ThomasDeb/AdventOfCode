# import numpy as np
#
# f = open("input18.txt", "r")
# obstacles = []
# i = 0
# for line in f:
#     line_split = line.split(",")
#     obstacles.append((int(line_split[0]), int(line_split[1])))
#     i += 1
# n_obstacles = i
#
# size_memory = 71
# n_bytes = 1024
# memory = np.zeros((size_memory, size_memory))
# for n in range(n_bytes):
#     i, j = obstacles[n][0], obstacles[n][1]
#     memory[i, j] = 1
# memory[0, 0] = -1
#
# possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# def idx_in_range(i, j):
#     if i >= 0 and i < size_memory and j >= 0 and j < size_memory:
#         return True
#     else:
#         return False
#
# coordinates = [(0, 0)]
# num_steps = 0
# while True:
#     next_coordinates = []
#     for idx in range(len(coordinates)):
#         i, j = coordinates[idx]
#         for (di, dj) in possible_directions:
#             if idx_in_range(i + di, j + dj) and memory[i + di, j + dj] == 0:
#                     next_coordinates.append((i + di, j + dj))
#
#     next_coordinates = list(set(next_coordinates))
#     coordinates = next_coordinates
#     num_steps += 1
#     if (70, 70) in coordinates:
#         break
#
# print(num_steps)
import matplotlib.pyplot as plt
import numpy as np

f = open("input18.txt", "r")
obstacles = []
i = 0
for line in f:
    line_split = line.split(",")
    obstacles.append((int(line_split[0]), int(line_split[1])))
    i += 1
n_obstacles = i

size_memory = 71


n_bytes = 2048
memory = np.zeros((size_memory, size_memory))
for n in range(n_bytes):
    i, j = obstacles[n][0], obstacles[n][1]
    memory[i, j] = 1
memory[0, 0] = -1

possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def idx_in_range(i, j):
    if i >= 0 and i < size_memory and j >= 0 and j < size_memory:
        return True
    else:
        return False

def is_possible(n_bytes):
    out = False
    coordinates = [(0, 0)]
    explored = [(0, 0)]
    num_steps = 0
    while coordinates:
        next_coordinates = []
        for idx in range(len(coordinates)):
            i, j = coordinates[idx]
            for (di, dj) in possible_directions:
                if idx_in_range(i + di, j + dj) and (i + di, j + dj) not in obstacles[:n_bytes] and (i + di, j + dj) not in explored:
                        next_coordinates.append((i + di, j + dj))

        next_coordinates = list(set(next_coordinates))
        coordinates = next_coordinates
        explored.extend(coordinates)
        num_steps += 1
        if (70, 70) in coordinates:
            return True
    return False

a, b = 2048, len(obstacles) - 1

while b - a > 1:
    c = int((a + b) / 2)
    if is_possible(c):
        a = c
    else:
        b = c

print(b)


memory = np.zeros((size_memory, size_memory))
for n in range(b):
    i, j = obstacles[n][0], obstacles[n][1]
    memory[i, j] = 1

plt.imshow(memory)
plt.show()

