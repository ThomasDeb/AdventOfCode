# f = open("input11.txt", "r")
#
# for line in f:
#     stones = line.split()
#
# n_blinks = 25
#
# for n in range(n_blinks):
#     print(n)
#     stones_prev = stones
#     stones = []
#     for stone in stones_prev:
#         if stone == "0":
#             stones.append("1")
#         elif len(stone) % 2 == 0:
#             stones.append(stone[:len(stone) // 2])
#             stones.append(str(int(stone[len(stone) // 2:])))
#         else:
#             stones.append(str(int(stone) * 2024))
#
# print(len(stones))

f = open("input11.txt", "r")

for line in f:
    stones = line.split()

n_blinks = 75
stones_count = {stones[i]: 1 for i in range(len(stones))}
s = 0
for n in range(n_blinks):
    print(n)
    stones_count_prev = stones_count
    stones_count = {}
    for stone, count in stones_count_prev.items():
        if stone == "0":
            if "1" not in stones_count.keys():
                stones_count["1"] = count
            else:
                stones_count["1"] += count

        elif len(stone) % 2 == 0:
            s1 = stone[:len(stone) // 2]
            s2 = str(int(stone[len(stone) // 2:]))
            if s1 not in stones_count.keys():
                stones_count[s1] = count
            else:
                stones_count[s1] += count
            if s2 not in stones_count.keys():
                stones_count[s2] = count
            else:
                stones_count[s2] += count
        else:
            s = str(int(stone) * 2024)
            if s not in stones_count.keys():
                stones_count[s] = count
            else:
                stones_count[s] += count


print(sum(stones_count.values()))