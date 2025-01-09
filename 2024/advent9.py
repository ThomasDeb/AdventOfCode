# f = open("input9.txt", "r")
#
# for line in f:
#     disk_map = line
# disk_map = disk_map[:-1]
#
# blocks = []
# for i in range(len(disk_map) // 2):
#     blocks.extend([i for _ in range(int(disk_map[2 * i]))])
#     blocks.extend("." * int(disk_map[2 * i + 1]))
# if len(disk_map) % 2 == 1:
#     blocks.extend([(len(disk_map) - 1) // 2 for _ in range(int(disk_map[-1]))])
#
# blocks_no_space = [i for i in blocks if i != "."]
#
# idx_up = 0
# idx_down = len(blocks_no_space) - 1
# block_id = 0
# while block_id <= blocks_no_space[idx_down]:
#     if block_id == blocks_no_space[idx_down]:
#         while block_id == blocks_no_space[idx_down]:
#             idx_up += 1
#             idx_down -= 1
#         del blocks[idx_up:]
#         break
#     idx_up = blocks.index(".", idx_up)
#     block_id = blocks[idx_up - 1]
#     while blocks[idx_up] == ".":
#         if blocks_no_space[idx_down] <= block_id:
#             del blocks[idx_up:]
#             break
#         blocks[idx_up] = blocks_no_space[idx_down]
#         idx_up += 1
#         idx_down -= 1
#
# if "." in blocks:
#      idx = blocks.index(".", idx_up)
#      del blocks[idx:]
#
# diff = blocks.count(blocks[-1]) - blocks_no_space.count(blocks[-1])
# if diff > 0:
#     del blocks[-diff:]
#
#
#
# s = sum([i * blocks[i] for i in range(len(blocks))])
# print(s)

f = open("input9.txt", "r")

for line in f:
    disk_map = line
disk_map = disk_map[:-1]

blocks = []
for i in range(len(disk_map) // 2):
    blocks.extend([i for _ in range(int(disk_map[2 * i]))])
    blocks.extend("." * int(disk_map[2 * i + 1]))
if len(disk_map) % 2 == 1:
    blocks.extend([(len(disk_map) - 1) // 2 for _ in range(int(disk_map[-1]))])

idx_down = len(blocks) - 1
is_end = True
while idx_down > 0:
    id = blocks[idx_down]
    file_size = 0
    while idx_down >= 0 and blocks[idx_down] == id:
        file_size += 1
        idx_down -= 1
    if idx_down < 0:
        break
    is_space = [blocks[idx: idx + file_size] == ["." for _ in range(file_size)] for idx in range(idx_down)]
    if any(is_space):
        idx = is_space.index(True)
        blocks[idx: idx + file_size] = [id for _ in range(file_size)]
        blocks[idx_down + 1: idx_down + 1 + file_size] = ["." for _ in range(file_size)]
    while blocks[idx_down] == ".":
        idx_down -= 1


s = sum([i * blocks[i] if blocks[i] != "." else 0 for i in range(len(blocks))])
print(s)
