#
# f = open("input10.txt", "r")
#
#
# map = []
# counts = []
# ni = 0
# for line in f:
#     map.append([int(line[i]) for i in range(len(line.strip()))])
#     counts.append([1 for _ in range(len(line.strip()))])
#     ni += 1
# nj = len(map[1])
#
#
# def reachable_neighbor(i, j, n):
#     neighbors = []
#     if i > 0 and map[i - 1][j] == n:
#         neighbors.append((i - 1, j))
#     if j > 0 and map[i][j - 1] == n:
#         neighbors.append((i, j - 1))
#     if i < ni - 1 and map[i + 1][j] == n:
#         neighbors.append((i + 1, j))
#     if j < nj - 1 and map[i][j + 1] == n:
#         neighbors.append((i, j + 1))
#     return neighbors
#
# s = 0
# for i in range(ni):
#     for j in range(nj):
#         if map[i][j] == 0:
#             reachable_locs = [(i, j)]
#             for n in range(1, 10):
#                 neighbors = []
#                 for (ii, jj) in reachable_locs:
#                     neighbors.extend(reachable_neighbor(ii, jj, n))
#                 reachable_locs = list(set(neighbors))
#                 if n == 9:
#                     s += len(reachable_locs)
#
# print(s)


f = open("input10.txt", "r")


map = []
counts = []
ni = 0
for line in f:
    map.append([int(line[i]) for i in range(len(line.strip()))])
    counts.append([1 for _ in range(len(line.strip()))])
    ni += 1
nj = len(map[1])

def neighbor_count(i, j, n):
    c = 0
    if i > 0 and map[i - 1][j] == n:
        c += counts[i - 1][j]
    if j > 0 and map[i][j - 1] == n:
        c += counts[i][j - 1]
    if i < ni - 1 and map[i + 1][j] == n:
        c += counts[i + 1][j]
    if j < nj - 1 and map[i][j + 1] == n:
        c += counts[i][j + 1]
    return c

s = 0
for n in range(8, -1, -1):
    for i in range(ni):
        for j in range(nj):
            if map[i][j] == n:
                counts[i][j] = neighbor_count(i, j, n + 1)
                if n == 0:
                    s += counts[i][j]

print(s)