# f = open("input12.txt", "r")
#
#
# def is_neighbor(x1, y1, x2, y2):
#     if x1 == x2 and abs(y2 - y1) == 1:
#         return True
#     if y1 == y2 and abs(x2 - x1) == 1:
#         return True
#     return False
#
#
# region_types = []
# region_coordinates = []
# i = 0
# for line in f:
#     line = line.strip()
#     for j in range(len(line)):
#         neighbor_region_idx = -1
#         if line[j] in region_types:
#             indices = [idx for (idx, x) in enumerate(region_types) if x == line[j]]
#             for idx in indices:
#                 for (i1, j1) in region_coordinates[idx]:
#                     if is_neighbor(i, j, i1, j1):
#                         if neighbor_region_idx >= 0:
#                             region_coordinates[neighbor_region_idx].extend(region_coordinates[idx])
#                             del region_coordinates[idx]
#                             del region_types[idx]
#                             neighbor_region_idx = (neighbor_region_idx, idx)
#                         else:
#                             region_coordinates[idx].append((i, j))
#                             neighbor_region_idx = idx
#                         break
#                 if type(neighbor_region_idx) != int:
#                     break
#         if neighbor_region_idx == -1:
#             region_types.append(line[j])
#             region_coordinates.append([(i, j)])
#
#     i += 1
#
# s = 0
# for region in region_coordinates:
#     perimeter = 0
#     area = 0
#     for (i, j) in region:
#         area += 1
#         if (i - 1, j) not in region:
#             perimeter += 1
#         if (i + 1, j) not in region:
#             perimeter += 1
#         if (i, j - 1) not in region:
#             perimeter += 1
#         if (i, j + 1) not in region:
#             perimeter += 1
#     s += perimeter * area
#
# print(s)
#

f = open("input12.txt", "r")


def is_neighbor(x1, y1, x2, y2):
    if x1 == x2 and abs(y2 - y1) == 1:
        return True
    if y1 == y2 and abs(x2 - x1) == 1:
        return True
    return False


region_types = []
region_coordinates = []
i = 0
for line in f:
    line = line.strip()
    for j in range(len(line)):
        neighbor_region_idx = -1
        if line[j] in region_types:
            indices = [idx for (idx, x) in enumerate(region_types) if x == line[j]]
            for idx in indices:
                for (i1, j1) in region_coordinates[idx]:
                    if is_neighbor(i, j, i1, j1):
                        if neighbor_region_idx >= 0:
                            region_coordinates[neighbor_region_idx].extend(region_coordinates[idx])
                            del region_coordinates[idx]
                            del region_types[idx]
                            neighbor_region_idx = (neighbor_region_idx, idx)
                        else:
                            region_coordinates[idx].append((i, j))
                            neighbor_region_idx = idx
                        break
                if type(neighbor_region_idx) != int:
                    break
        if neighbor_region_idx == -1:
            region_types.append(line[j])
            region_coordinates.append([(i, j)])

    i += 1

s = 0
for region in region_coordinates:
    perimeter = 0
    area = 0
    for (i, j) in region:
        area += 1
        if (i - 1, j) not in region:
            if ((i, j - 1) not in region) or ((i - 1, j - 1) in region):
                perimeter += 1
        if (i + 1, j) not in region:
            if ((i, j - 1) not in region) or ((i + 1, j - 1) in region):
                perimeter += 1
        if (i, j - 1) not in region:
            if ((i - 1, j) not in region) or ((i - 1, j - 1) in region):
                perimeter += 1
        if (i, j + 1) not in region:
            if ((i - 1, j) not in region) or ((i - 1, j + 1) in region):
                perimeter += 1
    s += perimeter * area

print(s)

