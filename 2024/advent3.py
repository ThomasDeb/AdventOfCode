# import re
#
# f = open("input3.txt", "r")
#
# s = 0
# for line in f:
#     indices_start = [m.start() for m in re.finditer("mul\(", line)]
#     for idx in indices_start:
#         i = idx + 4
#         num1 = ""
#         while line[i].isdigit():
#             num1 += line[i]
#             i += 1
#         if line[i] == ",":
#             i += 1
#             num2 = ""
#             while line[i].isdigit():
#                 num2 += line[i]
#                 i += 1
#             if line[i] == ")" and num1 and num2:
#                 s += int(num1) * int(num2)
#
# print(s)

import re


def is_do_idx(idx, indices_do, indices_dont, is_do):
    if not indices_do:
        if (not indices_dont) or (idx < indices_dont[0]):
            return is_do
        else:
            return False
    else:
        indices_do_prev = list(filter(lambda x: (x < idx), indices_do))
        if not indices_dont:
            return len(indices_do_prev) != 0
        else:
            indices_dont_prev = list(filter(lambda x: (x < idx), indices_dont))
            if indices_do_prev:
                if indices_dont_prev and (indices_dont_prev[-1] > indices_do_prev[-1]):
                    return False
                else:
                    return True
            else:
                if indices_dont_prev:
                    return False
                else:
                    return is_do

f = open("input3.txt", "r")

s = 0
is_do = True
for line in f:
    indices_mul = [m.start() for m in re.finditer("mul\(", line)]
    indices_do = [m.start() for m in re.finditer("do\(\)", line)]
    indices_dont = [m.start() for m in re.finditer("don\'t\(\)", line)]
    for idx in indices_mul:
        if is_do_idx(idx, indices_do, indices_dont, is_do):
            i = idx + 4
            num1 = ""
            while line[i].isdigit():
                num1 += line[i]
                i += 1
            if line[i] == ",":
                i += 1
                num2 = ""
                while line[i].isdigit():
                    num2 += line[i]
                    i += 1
                if line[i] == ")" and num1 and num2:
                    s += int(num1) * int(num2)
    if indices_do:
        if indices_dont:
            is_do = indices_do[-1] > indices_dont[-1]
        else:
            is_do = True
    else:
        if indices_dont:
            is_do = False

print(s)




