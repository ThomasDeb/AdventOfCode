# f = open("input1.txt", "r")
#
# left_list, right_list = [], []
# for line in f:
#     line_split = line.split()
#     left_list.append(int(line_split[0]))
#     right_list.append(int(line_split[1]))
#
# left_list.sort()
# right_list.sort()
#
# distances = []
# for i in range(len(left_list)):
#     distances.append(abs(left_list[i] - right_list[i]))
#
# s = sum(distances)
# print(s)

f = open("input1.txt", "r")

left_list, right_list = [], []
for line in f:
    line_split = line.split()
    left_list.append(int(line_split[0]))
    right_list.append(int(line_split[1]))

left_list.sort()
right_list.sort()

s = 0
for i in range(len(left_list)):
    s += left_list[i] * right_list.count(left_list[i])

print(s)




