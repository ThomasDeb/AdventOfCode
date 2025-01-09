# f = open("input5.txt", "r")
#
# seeds = f.readline().split()[1:]
# seeds = [int(seed) for seed in seeds]
#
# for line in f:
#     if "map:" in line:
#         modified_seeds = []
#     elif any(char.isdigit() for char in line):
#         line_split = [int(n) for n in line.split()]
#         start_dest, start_source, rng = tuple(line_split)
#         for i in range(len(seeds)):
#             if (start_source <= seeds[i] < start_source + rng) and (i not in modified_seeds):
#                 seeds[i] = start_dest + (seeds[i] - start_source)
#                 modified_seeds.append(i)
#
# print(min(seeds))

def intersection(seed, seed_len, start_dest, start_source, map_len):
    seeds_sm = []
    seeds_mod = []
    if seed < start_source <= seed + seed_len - 1:
        seeds_sm.extend([seed, start_source - seed])
        if seed + seed_len - 1 < start_source + map_len:
            seeds_mod = [start_dest, seed_len - (start_source - seed)]
        else:
            seeds_mod = [start_dest, map_len]
            seeds_sm.extend([start_source + map_len, seed_len - map_len - (start_source - seed)])
    elif seed < start_source + map_len and start_source <= seed + seed_len - 1:
        if seed + seed_len - 1 < start_source + map_len:
            seeds_mod = [start_dest + (seed - start_source), seed_len]
        else:
            seeds_mod = [start_dest + (seed - start_source), map_len - (seed - start_source)]
            seeds_sm.extend([start_source + map_len, seed_len - (map_len - (seed - start_source))])
    else:
        seeds_sm.extend([seed, seed_len])

    return seeds_sm, seeds_mod

f = open("input5.txt", "r")

seeds = f.readline().split()[1:]
seeds = [int(seed) for seed in seeds]
seeds_prev = []

for line in f:
    if "map:" in line:
        seeds.extend(seeds_prev)
        seeds_prev_temp = seeds.copy()
        seeds = []
    elif any(char.isdigit() for char in line):
        line_split = [int(n) for n in line.split()]
        seeds_prev = seeds_prev_temp.copy()
        seeds_prev_temp = []
        for n in range(len(seeds_prev) // 2):
            seeds_same, seeds_modified = intersection(seeds_prev[2 * n], seeds_prev[2 * n + 1], *line_split)
            seeds.extend(seeds_modified)
            seeds_prev_temp.extend(seeds_same)

        seeds_prev = seeds_prev_temp.copy()

seeds.extend(seeds_prev)
print(min(seeds[::2]))
