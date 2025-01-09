# f = open("input6.txt", "r")
#
# s = 0
# i = 0
# obstacles = []
# for line in f:
#     for j in range(len(line)):
#         if line[j] == "#":
#             obstacles.append((i, j))
#     if "^" in line:
#         j = line.index("^")
#         guard_position = (i, j)
#         nj = len(line)
#     i+= 1
#
# ni = i
#
# path = [guard_position]
# direction = (-1, 0)
# while True:
#     next_position = (guard_position[0] + direction[0], guard_position[1] + direction[1])
#     if next_position in obstacles:
#         is_obstacle = True
#         if direction[0] == 0:
#             direction = (direction[1], 0)
#         else:
#             direction = (0, -direction[0])
#     elif (next_position[0] == -1) or (next_position[0] == ni) or (next_position[1] == -1) or (next_position[1] == nj):
#         break
#     else:
#         guard_position = next_position
#         path.append(guard_position)
#
# s = len(set(path))
# print(s)

f = open("input6.txt", "r")

i = 0
obstacles = []
for line in f:
    for j in range(len(line)):
        if line[j] == "#":
            obstacles.append((i, j))
    if "^" in line:
        j = line.index("^")
        guard_position0 = (i, j)
        nj = len(line)
    i+= 1

ni = i

guard_position = guard_position0
path0 = [guard_position0]
direction = (-1, 0)
directions0 = [direction]
while True:
    next_position = (guard_position[0] + direction[0], guard_position[1] + direction[1])
    if next_position in obstacles:
        is_obstacle = True
        if direction[0] == 0:
            direction = (direction[1], 0)
        else:
            direction = (0, -direction[0])
    elif (next_position[0] == -1) or (next_position[0] == ni) or (next_position[1] == -1) or (next_position[1] == nj):
        break
    else:
        guard_position = next_position
        path0.append(guard_position)
        directions0.append(direction)

path0 = list(set(path0))

s = 0
for (i, j) in path0[1:]:
    obstacles.append((i, j))
    guard_position = guard_position0
    path = [guard_position]
    direction = (-1, 0)
    directions = [direction]
    while True:
        next_position = (guard_position[0] + direction[0], guard_position[1] + direction[1])
        if next_position in obstacles:
            is_obstacle = True
            if direction[0] == 0:
                direction = (direction[1], 0)
            else:
                direction = (0, -direction[0])
        elif (next_position[0] == -1) or (next_position[0] == ni) or (next_position[1] == -1) or (next_position[1] == nj):
            obstacles.pop()
            break
        else:
            guard_position = next_position
            if ((guard_position, direction) in zip(path, directions)):
                obstacles.pop()
                s += 1
                break
            path.append(guard_position)
            directions.append(direction)
print(s)