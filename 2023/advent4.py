# f = open("input4.txt", "r")
# s = 0
#
# for line in f:
#     line_split = line[10:-1].split("|")
#     winning_numbers = line_split[0].split()
#     card = line_split[1].split()
#     num_wins = 0
#     for number in card:
#         if number in winning_numbers:
#             num_wins += 1
#     if num_wins > 0:
#         s += 2 ** (num_wins - 1)
#
# print(s)

f = open("input4.txt", "r")
s = 0
copies = [1]
line_num = 0

for line in f:
    line_split = line[10:-1].split("|")
    winning_numbers = line_split[0].split()
    card = line_split[1].split()
    num_wins = 0
    for number in card:
        if number in winning_numbers:
            num_wins += 1
            if len(copies) <= line_num + num_wins:
                copies.append(1)
            copies[line_num + num_wins] += copies[line_num]
    if len(copies) == line_num + 1:
        copies.append(1)
    line_num += 1

s = sum(copies[:line_num])
print(s)
