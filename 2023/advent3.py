f = open("input3.txt", "r")
sym_coord = []
part_coord = []


# def is_adjacent(sym_idx, part):
#     if part[1] - 1 <= sym_idx <= part[2] + 1:
#         return True
#     else:
#         return False
#
#
# line_idx = 0
# for line in f:
#     sym_coord.append([])
#     part_coord.append([])
#     symbols = []
#     char_idx = 0
#     num = ""
#     for char in line.strip():
#         if char.isdigit():
#             num += char
#         elif char != ".":
#             sym_coord[line_idx].append(char_idx)
#         if len(num) > 0 and (not char.isdigit() or char_idx == len(line.strip()) - 1):
#             if char.isdigit() and (char_idx == len(line.strip()) - 1):
#                 char_idx += 1
#             part_coord[line_idx].append((int(num), char_idx - len(num), char_idx - 1))
#             num = ""
#         char_idx += 1
#     test, test1 = part_coord[line_idx], sym_coord[line_idx]
#     line_idx += 1

# s = 0
# num_adj, num_non_adj = 0, 0
# for n in range(len(part_coord)):
#     if n == 0:
#         adj_sym = [*sym_coord[n], *sym_coord[n + 1]]
#     elif n == len(sym_coord) - 1:
#         adj_sym = [*sym_coord[n - 1], *sym_coord[n]]
#     else:
#         adj_sym = [*sym_coord[n - 1], *sym_coord[n], *sym_coord[n + 1]]
#
#     for part in part_coord[n]:
#         for sym_idx in adj_sym:
#             if is_adj := is_adjacent(sym_idx, part):
#                 break
#         if is_adj:
#             s += part[0]
#             num_adj += 1
#         else:
#             num_non_adj += 1

# print(s)

def is_adjacent(sym_idx, part):
    if part[1] - 1 <= sym_idx <= part[2] + 1:
        return True
    else:
        return False


line_idx = 0
for line in f:
    sym_coord.append([])
    part_coord.append([])
    symbols = []
    char_idx = 0
    num = ""
    for char in line.strip():
        if char.isdigit():
            num += char
        elif char == "*":
            sym_coord[line_idx].append(char_idx)
        if len(num) > 0 and (not char.isdigit() or char_idx == len(line.strip()) - 1):
            if char.isdigit() and (char_idx == len(line.strip()) - 1):
                char_idx += 1
            part_coord[line_idx].append((int(num), char_idx - len(num), char_idx - 1))
            num = ""
        char_idx += 1
    test, test1 = part_coord[line_idx], sym_coord[line_idx]
    line_idx += 1

s = 0
num_adj, num_non_adj = 0, 0
for n in range(len(sym_coord)):
    if n == 0:
        adj_part = [*part_coord[n], *part_coord[n + 1]]
    elif n == len(sym_coord) - 1:
        adj_part = [*part_coord[n - 1], *part_coord[n]]
    else:
        adj_part = [*part_coord[n - 1], *part_coord[n], *part_coord[n + 1]]
    for sym in sym_coord[n]:
        num_adj_part = 0
        prod = 1
        for part in adj_part:
            if is_adj := is_adjacent(sym, part):
                num_adj_part += 1
                prod *= part[0]
        if num_adj_part == 2:
            s += prod


print(s)





