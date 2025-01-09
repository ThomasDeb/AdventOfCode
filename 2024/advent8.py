# from itertools import combinations
#
# f = open("input8.txt", "r")
#
# antennas = {}
# i = 0
# for line in f:
#     if i == 0:
#         nj = len(line) - 1
#     for j in range(nj):
#         if line[j] != ".":
#             if line[j] in antennas.keys():
#                 antennas[line[j]].append((i, j))
#             else:
#                 antennas[line[j]] = [(i, j)]
#     i += 1
#
# ni = i
#
# antinodes = []
# for key in antennas.keys():
#     for comb in combinations(antennas[key], 2):
#         (i1, j1) = comb[0]
#         (i2, j2) = comb[1]
#         (ii1, jj1) = (i1 - (i2 - i1), j1 - (j2 - j1))
#         (ii2, jj2) = (i2 + (i2 - i1), j2 + (j2 - j1))
#         for (i, j) in [(ii1, jj1), (ii2, jj2)]:
#             if ((i, j) not in antinodes) and (i >= 0 and i < ni and j >= 0 and j < nj):
#                 antinodes.append((i, j))
#
# print(len(antinodes))

from itertools import combinations

f = open("input8.txt", "r")

antennas = {}
i = 0
for line in f:
    if i == 0:
        nj = len(line) - 1
    for j in range(nj):
        if line[j] != ".":
            if line[j] in antennas.keys():
                antennas[line[j]].append((i, j))
            else:
                antennas[line[j]] = [(i, j)]
    i += 1

ni = i

antinodes = []
for key in antennas.keys():
    for comb in combinations(antennas[key], 2):
        (i1, j1) = comb[0]
        (i2, j2) = comb[1]

        k_min = - i1 // (i2 - i1)
        k_max = (ni - i1) // (i2 - i1)
        if i2 < i1:
            k_min, k_max = k_max, k_min
        for k in range(k_min, k_max + 1):
            i = i1 + k * (i2 - i1)
            j = j1 + k * (j2 - j1)
            if ((i, j) not in antinodes) and (i >= 0 and i < ni and j >= 0 and j < nj):
                antinodes.append((i, j))
            k += 1

print(len(antinodes))

