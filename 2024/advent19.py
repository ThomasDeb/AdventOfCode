# f = open("input19.txt", "r")
# patterns = []
# i = 0
# for line in f:
#     line_strip = line.strip()
#     if i == 0:
#         towels = line_strip.replace(" ", "").split(",")
#     else:
#         if line_strip:
#             patterns.append(line.strip())
#     i += 1
#
# n_possible = 0
#
# for pattern in patterns:
#     possible_arrangements = [""]
#     is_possible = False
#     while (not is_possible) and (possible_arrangements):
#         next_possible_arrangements = []
#         for arrangement in possible_arrangements:
#             idx = len(arrangement)
#             for towel in towels:
#                 if idx + len(towel) <= len(pattern) and towel == pattern[idx: idx + len(towel)]:
#                     if (new_arrangement:= arrangement + towel) == pattern:
#                         is_possible = True
#                         break
#                     else:
#                         next_possible_arrangements.append(new_arrangement)
#             if is_possible:
#                 break
#         possible_arrangements = list(set(next_possible_arrangements))
#     if is_possible:
#         n_possible += 1
#
# print(n_possible)

f = open("input19.txt", "r")
patterns = []
i = 0
for line in f:
    line_strip = line.strip()
    if i == 0:
        towels = line_strip.replace(" ", "").split(",")
    else:
        if line_strip:
            patterns.append(line.strip())
    i += 1

n_possible = 0
n_pattern = 0
for pattern in patterns:
    print(n_pattern)
    possible_arrangements = {"": 1}
    while possible_arrangements:
        next_possible_arrangements = {}
        for arrangement in possible_arrangements.keys():
            idx = len(arrangement)
            for towel in towels:
                if idx + len(towel) <= len(pattern) and towel == pattern[idx: idx + len(towel)]:
                    if (new_arrangement:= arrangement + towel) == pattern:
                        n_possible += possible_arrangements[arrangement]
                    else:
                        if new_arrangement in next_possible_arrangements.keys():
                            next_possible_arrangements[new_arrangement] += possible_arrangements[arrangement]
                        else:
                            next_possible_arrangements[new_arrangement] = possible_arrangements[arrangement]
        possible_arrangements = next_possible_arrangements
    n_pattern += 1

print(n_possible)