# f = open("input13.txt", "r")
#
# def solve_pb(xa, ya, xb, yb, x_prize, y_prize):
#     cost = 0
#     for na in range(101):
#         nbx = (x_prize - na * xa) / xb
#         nby = (y_prize - na * ya) / yb
#         if nbx.is_integer() and nby.is_integer() and nbx == nby:
#             cost = 3 * na + int(nbx)
#             break
#     return cost
#
# s = 0
# for line in f:
#     line_split = line.split()
#     if "Button A" in line:
#         xa = int(line_split[2][2:-1])
#         ya = int(line_split[3][2:])
#     elif "Button B" in line:
#         xb = int(line_split[2][2:-1])
#         yb = int(line_split[3][2:])
#     elif "Prize" in line:
#         x_prize = int(line_split[1][2:-1])
#         y_prize = int(line_split[2][2:])
#         s += solve_pb(xa, ya, xb, yb, x_prize, y_prize)
#
# print(s)

f = open("input13.txt", "r")

def solve_pb(xa, ya, xb, yb, x_prize, y_prize):
    cost = 0
    det = xa * yb - xb * ya
    if det == 0:
        if xa * y_prize == ya * x_prize:
            pass
    else:
        na = (x_prize * yb - y_prize * xb) / det
        nb = - (x_prize * ya - y_prize * xa) / det
        if na.is_integer() and nb.is_integer() and na >= 0 and nb >= 0:
            cost = 3 * int(na) + int(nb)
    return cost

s = 0
for line in f:
    line_split = line.split()
    if "Button A" in line:
        xa = int(line_split[2][2:-1])
        ya = int(line_split[3][2:])
    elif "Button B" in line:
        xb = int(line_split[2][2:-1])
        yb = int(line_split[3][2:])
    elif "Prize" in line:
        x_prize = int(line_split[1][2:-1]) + int(1e13)
        y_prize = int(line_split[2][2:]) + int(1e13)
        s += solve_pb(xa, ya, xb, yb, x_prize, y_prize)

print(s)