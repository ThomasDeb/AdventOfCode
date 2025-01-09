# f = open("input4.txt", "r")
#
# s = 0
# input_txt = []
# for line in f:
#     input_txt.append(line)
# num_lines = len(input_txt)
# num_col = len(input_txt[0])
#
# for i in range(num_lines):
#     for j in range(num_col):
#         if input_txt[i][j] == "X":
#             if (j < num_col - 3) and input_txt[i][j + 1 : j + 4] == "MAS":
#                 s += 1
#             if (j >= 3) and input_txt[i][j - 3 : j] == "SAM":
#                 s += 1
#             if (i < num_lines - 3) and (input_txt[i + 1][j]) == "M" and (input_txt[i + 2][j] == "A") and (input_txt[i + 3][j] == "S"):
#                 s += 1
#             if (i >= 3) and (input_txt[i - 1][j] == "M") and (input_txt[i - 2][j] == "A") and (input_txt[i - 3][j] == "S"):
#                 s += 1
#             if (j < num_col - 3) and (i < num_lines - 3) and (input_txt[i + 1][j + 1] == "M") and (input_txt[i + 2][j + 2] == "A") and (input_txt[i + 3][j + 3] == "S"):
#                 s += 1
#             if (j < num_col - 3) and (i >= 3) and (input_txt[i - 1][j + 1] == "M") and (input_txt[i - 2][j + 2] == "A") and (input_txt[i - 3][j + 3] == "S"):
#                 s += 1
#             if (j >= 3) and (i < num_lines - 3) and (input_txt[i + 1][j - 1] == "M") and (input_txt[i + 2][j - 2] == "A") and (input_txt[i + 3][j - 3] == "S"):
#                 s += 1
#             if (j >= 3) and (i >= 3) and (input_txt[i - 1][j - 1] == "M") and (input_txt[i - 2][j - 2] == "A") and (input_txt[i - 3][j - 3] == "S"):
#                 s += 1
#
# print(s)

f = open("input4.txt", "r")

s = 0
input_txt = []
for line in f:
    input_txt.append(line)
num_lines = len(input_txt)
num_col = len(input_txt[0])

for i in range(1, num_lines - 1):
    for j in range(1, num_col - 1):
        if input_txt[i][j] == "A":
            if (input_txt[i - 1][j - 1] == "M" and input_txt[i + 1][j + 1] == "S") or (input_txt[i - 1][j - 1] == "S" and input_txt[i + 1][j + 1] == "M"):
                if (input_txt[i - 1][j + 1] == "M" and input_txt[i + 1][j - 1] == "S") or (input_txt[i - 1][j + 1] == "S" and input_txt[i + 1][j - 1] == "M"):
                    s += 1

print(s)
