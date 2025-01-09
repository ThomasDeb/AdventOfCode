# f = open("input2.txt", "r")
#
# s = 0
# for line in f:
#     line_split = line.split()
#     line_split = [int(level) for level in line_split]
#     if line_split[::-1] == sorted(line_split):
#         line_split.sort()
#     if line_split == sorted(line_split):
#         is_safe = True
#         for i in range(len(line_split) - 1):
#             if (line_split[i + 1] - line_split[i] < 1) or (line_split[i + 1] - line_split[i] > 3):
#                 is_safe = False
#         s += is_safe
#
# print(s)

def is_safe(report):
    out = False
    report_copy = report.copy()
    if report[::-1] == sorted(report):
        report_copy = report[::-1]
    if report_copy == sorted(report):
        out = True
        for i in range(len(report) - 1):
            if (report_copy[i + 1] - report_copy[i] < 1) or (report_copy[i + 1] - report_copy[i] > 3):
                out = False
    return out


f = open("input2.txt", "r")
s = 0
for line in f:
    line_split = line.split()
    line_split = [int(level) for level in line_split]
    safe = False
    if is_safe(line_split):
        safe = True
    else:
        for i in range(len(line_split)):
            line_copy = line_split.copy()
            del line_copy[i]
            if is_safe(line_copy):
                safe = True
    s += safe

print(s)





