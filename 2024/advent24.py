# def do_operation(x, y, op):
#     if op == "AND":
#         return (x and y)
#     elif op == "OR":
#         return (x or y)
#     elif op == "XOR":
#         return (x ^ y)
#
#
# f = open("input24.txt", "r")
# known_values = {}
# incomplete_lines = []
# for line in f:
#     line_strip = line.strip()
#     if ":" in line_strip:
#         l = line_strip.replace(" ", "").split(":")
#         known_values[l[0]] = int(l[1])
#     if "->" in line_strip:
#         line_split = line_strip.split()
#         del line_split[3]
#         if line[0] not in known_values.keys() or line_split[2] not in known_values.keys():
#             incomplete_lines.append(tuple(line_split))
#         else:
#             x, y = known_values[line[0]], known_values[line[2]]
#             known_values[line_split[3]] = do_operation(x, y, line_split[1])
#
# while incomplete_lines:
#     new_incomplete_lines = []
#     for line in incomplete_lines:
#         x_key, op, y_key, out = line
#         if x_key in known_values.keys() and y_key in known_values.keys():
#             x, y = known_values[x_key], known_values[y_key]
#             known_values[out] = do_operation(x, y, op)
#         else:
#             new_incomplete_lines.append(line)
#     incomplete_lines = new_incomplete_lines
#
# z_key = "z00"
# out_binary = ""
# i = 0
# while z_key in known_values.keys():
#     out_binary = str(known_values[z_key]) + out_binary
#     i += 1
#     if i < 10:
#         z_key = "z0" + str(i)
#     else:
#         z_key = "z" + str(i)
#
# print(int(out_binary, 2))
#
from sympy.combinatorics.fp_groups import descendant_subgroups


def z_key(i):
    i += 1
    if i < 10:
        z_key = "z0" + str(i)
    else:
        z_key = "z" + str(i)

f = open("input24.txt", "r")
outputs = []
operations = []
descendants = {}
i = 0
for line in f:
    if "->" in line:
        line_split = line.split()
        del line_split[3]
        outputs.append(line_split[-1])
        operations.append(tuple(line_split[:-1]))
        descendants[line_split[-1]] = [line_split[0], line_split[2]], [i]
        i += 1

is_done = False
while not is_done:
    is_done = True
    for key in descendants.keys():
        desc, indices = descendants[key]
        new_desc = []
        new_indices = indices.copy()
        for d in desc:
            if d[0] != "x" and d[0] != "y":
                new_desc.extend(descendants[d][0])
                new_indices.extend(descendants[d][1])
                is_done = False
            else:
                new_desc.append(d)

        descendants[key] = new_desc, new_indices

lines_to_change = []
and_list, xor_list = [], []
for i in range(len(outputs)):
    if outputs[i][0] == "z":
        idx = outputs[i][1:]
        if int(idx) > 1 and int(idx) < 45:
            if operations[i][1] != "XOR":
                lines_to_change.append(i)
    elif operations[i][1] == "XOR":
        x1, x2 = operations[i][0], operations[i][2]
        if x1[0] != "x" and x1[0] != "y":
            lines_to_change.append(i)
    if operations[i][1] == "OR":
        x1, x2 = operations[i][0], operations[i][2]
        for x in [x1, x2]:
            if len(descendants[x][0]) == 2:
                ii = descendants[x][1][0]
                if operations[ii][1] != "AND":
                    lines_to_change.append(ii)
                else:
                    and_list.append(operations[ii][0][1:])
        if len(descendants[x1][0]) != 2 and len(descendants[x2][0]) != 2:
            i1, i2 = outputs.index(x1), outputs.index(x2)
            # lines_to_change.append((i1, i2))
    elif operations[i][1] == "AND" :
        x1, x2 = operations[i][0], operations[i][2]
        if x1[0] != "x" and x1[0] != "y":
            for x in [x1, x2]:
                if len(descendants[x][0]) == 2:
                    ii = descendants[x][1][0]
                    if operations[ii][1] != "XOR" and operations[ii][0][1:] != "00":
                        lines_to_change.append(ii)
                    else:
                        xor_list.append(operations[ii][0][1:])

and_list.sort()
xor_list.sort()

lines_to_change = list(set(lines_to_change))
s = []
for i in lines_to_change:
    print(operations[i], outputs[i])
    s.append(outputs[i])
s.sort()
st = ""
for out in s:
    st += out + ","

print(st[:-1])
# descendants = {}
# for i in range(len(outputs)):
#     descendants[outputs[i]] = [operations[i][0], operations[i][2]], [i]
#
# is_done = False
# while not is_done:
#     is_done = True
#     for key in descendants.keys():
#         desc, indices = descendants[key]
#         new_desc = []
#         new_indices = indices.copy()
#         for d in desc:
#             if d[0] != "x" and d[0] != "y":
#                 new_desc.extend(descendants[d][0])
#                 new_indices.extend(descendants[d][1])
#                 is_done = False
#             else:
#                 new_desc.append(d)
#
#         descendants[key] = new_desc, new_indices








