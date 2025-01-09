# f = open("input5.txt", "r")
#
# s = 0
# order_before = []
# order_after = []
# updates = []
#
# for line in f:
#     if "|" in line:
#         line_split = line.split("|")
#         order_before.append(int(line_split[0]))
#         order_after.append(int(line_split[1]))
#     if "," in line:
#         line_split = line.split(",")
#         updates.append([int(num) for num in line_split])
#
# for update in updates:
#     is_correct = True
#     for i in range(len(update)):
#         indices = [idx for (idx, x) in enumerate(order_after) if x == update[i]]
#         for idx in indices:
#             if order_before[idx] in update[i:]:
#                 is_correct = False
#     if is_correct:
#         s += update[(len(update) - 1) // 2]
#
# print(s)

def swap_incorrect_indices(update):
    for i in range(len(update)):
        indices = [idx for (idx, x) in enumerate(order_after) if x == update[i]]
        for idx in indices:
            if order_before[idx] in update[i:]:
                j = update.index(order_before[idx], i)
                update[i], update[j] = update[j], update[i]
                return True
    return False


f = open("input5.txt", "r")

s = 0
order_before = []
order_after = []
updates = []

for line in f:
    if "|" in line:
        line_split = line.split("|")
        order_before.append(int(line_split[0]))
        order_after.append(int(line_split[1]))
    if "," in line:
        line_split = line.split(",")
        updates.append([int(num) for num in line_split])

for update in updates:
    is_incorrect = False
    while swap_incorrect_indices(update):
        is_incorrect = True
    if is_incorrect:
        s += update[(len(update) - 1) // 2]

print(s)