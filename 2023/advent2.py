f = open("input2.txt", "r")


def num_balls(balls, color):
    if color in balls:
        return int(balls[balls.index(color) - 1])
    else:
        return 0

# id = 1
# s = 0
# for line in f:
#     is_possible = True
#     list_reveals = line[:-1].split(':')[1].split(';')
#     for reveal in list_reveals:
#         balls = reveal.replace(",", "").split()
#         num_red = num_balls(balls, 'red')
#         num_green = num_balls(balls, 'green')
#         num_blue = num_balls(balls, 'blue')
#
#         if num_red > 12 or num_green > 13 or num_blue > 14:
#             is_possible = False
#     if is_possible:
#         s += id
#     id += 1
#
# print(s)

s = 0
for line in f:
    min_red, min_green, min_blue = 0, 0, 0
    list_reveals = line[:-1].split(':')[1].split(';')
    for reveal in list_reveals:
        balls = reveal.replace(",", "").split()
        num_red = num_balls(balls, 'red')
        num_green = num_balls(balls, 'green')
        num_blue = num_balls(balls, 'blue')

        min_red = max(num_red, min_red)
        min_green = max(num_green, min_green)
        min_blue = max(num_blue, min_blue)

    s += min_red * min_green * min_blue

print(s)
