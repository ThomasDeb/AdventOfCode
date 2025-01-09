# from itertools import product
#
# input_file_handle = open("input7.txt", "r")
#
# op = {'+': lambda x, y: x + y,
#       '*': lambda x, y: x * y}
#
# s = 0
# for line in input_file_handle:
#     line_split = line.split()
#     result = int(line_split[0][:-1])
#     comb = product(["+", "*"], repeat=len(line_split) - 2)
#     list_comb = list(comb)
#     for c in list_comb:
#         expr = int(line_split[1])
#         for i in range(len(line_split) - 2):
#             expr = op[c[i]](expr, int(line_split[i + 2]))
#         if expr == result:
#             s += result
#             break
#
# print(s)

from itertools import product

input_file_handle = open("input7.txt", "r")

op = {'+': lambda x, y: x + y,
      '*': lambda x, y: x * y,
      '||': lambda x, y: int(str(x) + str(y))}

s = 0
for line in input_file_handle:
    line_split = line.split()
    result = int(line_split[0][:-1])
    comb = product(["+", "*", "||"], repeat=len(line_split) - 2)
    list_comb = list(comb)
    for c in list_comb:
        expr = int(line_split[1])
        for i in range(len(line_split) - 2):
            expr = op[c[i]](expr, int(line_split[i + 2]))
        if expr == result:
            s += result
            break

print(s)