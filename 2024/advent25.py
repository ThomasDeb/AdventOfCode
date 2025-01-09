f = open("input25.txt", "r")

locks = []
keys = []
char = [".", "#"]
new_schema = True
for line in f:
    line_strip = line.strip()
    if line_strip:
        if new_schema:
            if line[0] == ".":
                top_char, bottom_char = ".", "#"
            else:
                top_char, bottom_char = "#", "."
            heights = [0 for _ in range(len(line_strip))]
            i = 0
            new_schema = False
        else:
            indices = [idx for (idx, x) in enumerate(line_strip) if x == "#"]
            if i < 5:
                for idx in indices:
                    heights[idx] += 1
            else:
                if top_char == ".":
                    keys.append(heights)
                else:
                    locks.append(heights)
                new_schema = True
            i += 1

s = 0
for heights1 in locks:
    for heights2 in keys:
        ds = 1
        for i in range(len(heights1)):
            if (heights1[i] + heights2[i]) > 5:
                ds = 0
                break
        s += ds
print(s)
