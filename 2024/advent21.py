#
# def row_col_numeric_keypad(key):
#     col0, col1, col2 = "x147", "0258", "A369"
#     if key in col0:
#         return col0.index(key), 0
#     elif key in col1:
#         return col1.index(key), 1
#     elif key in col2:
#         return col2.index(key), 2
#
#
# def row_col_directional_keypad(key):
#     row0, row1 = "<v>", "x^A"
#     if key in row0:
#         return 0, row0.index(key)
#     elif key in row1:
#         return 1, row1.index(key)
#
#
# def keypad_numeric(current_key, target_key):
#     keys = [""]
#     row_current, col_current = row_col_numeric_keypad(current_key)
#     row_target, col_target = row_col_numeric_keypad(target_key)
#     if col_current < col_target:
#         keys[0] += ">" * (col_target - col_current)
#     elif col_current > col_target and not (col_target == 0 and row_current == 0):
#         keys[0] += "<" * (col_current - col_target)
#     if row_current < row_target:
#         if keys[0] != "":
#             keys.append("^" * (row_target - row_current) + keys[0])
#         keys[0] += "^" * (row_target - row_current)
#     elif row_current > row_target:
#         if keys[0] != "" and not (col_current == 0 and row_target == 0):
#             keys.append("v" * (row_current - row_target) + keys[0])
#         keys[0] += "v" * (row_current - row_target)
#     if col_current > col_target and (col_target == 0 and row_current == 0):
#         keys[0] += "<" * (col_current - col_target)
#     return keys
#
# def keypad_directional(current_key, target_key):
#     keys = [""]
#     row_current, col_current = row_col_directional_keypad(current_key)
#     row_target, col_target = row_col_directional_keypad(target_key)
#     if col_current < col_target:
#         keys[0] += ">" * (col_target - col_current)
#     elif col_current > col_target and not (col_target == 0 and row_current == 1):
#         keys[0] += "<" * (col_current - col_target)
#     if row_current < row_target:
#         if keys[0] != "" and not col_current == 0:
#             keys.append("^" * (row_target - row_current) + keys[0])
#         keys[0] += "^" * (row_target - row_current)
#     elif row_current > row_target:
#         if keys[0] != "":
#             keys.append("v" * (row_current - row_target) + keys[0])
#         keys[0] += "v" * (row_current - row_target)
#     if col_current > col_target and (col_target == 0 and row_current == 1):
#         keys[0] += "<" * (col_current - col_target)
#     return keys
#
#
# def numeric_to_directional(code):
#     prev_key = "A"
#     sequences = [""]
#     for key in code:
#         next_sequences = []
#         for seq in sequences:
#             for s in keypad_numeric(prev_key, key):
#                 next_sequences.append(seq + s + "A")
#         prev_key = key
#         sequences = next_sequences
#     len_seq = min([len(s) for s in sequences])
#     sequences = [s for s in sequences if len(s) == len_seq]
#     return sequences
#
#
# def directional_to_directional(sequences):
#     prev_key = "A"
#     out = []
#     for sequence in sequences:
#         ss = [""]
#         for key in sequence:
#             next_ss = []
#             for seq in ss:
#                 for s in keypad_directional(prev_key, key):
#                     next_ss.append(seq + s + "A")
#             prev_key = key
#             ss = next_ss
#         out.extend(ss)
#     len_seq = min([len(s) for s in out])
#     out = [s for s in out if len(s) == len_seq]
#     return out
#
# def directional_to_directional_last(sequences):
#     prev_key = "A"
#     min_len = 1000
#     for sequence in sequences:
#         ss = [""]
#         for key in sequence:
#             next_ss = []
#             for seq in ss:
#                 for s in keypad_directional(prev_key, key):
#                     next_ss.append(seq + s + "A")
#             prev_key = key
#             ss = next_ss
#         lengths = [len(s) for s in ss]
#         new_min = min(lengths)
#         if new_min < min_len:
#             out = ss[lengths.index(new_min)]
#             min_len = new_min
#     return out
#
#
# f = open("input21.txt", "r")
# codes = []
# s = 0
# for line in f:
#     code = line.strip()
#     codes.append(code)
#     sequence_temp = directional_to_directional(numeric_to_directional(code))
#     sequence = directional_to_directional_last(sequence_temp)
#     min_len_seq = len(sequence)
#     print(sequence)
#     s += min_len_seq * int(code[:-1])
# print(s)
#


def row_col_numeric_keypad(key):
    col0, col1, col2 = "x147", "0258", "A369"
    if key in col0:
        return col0.index(key), 0
    elif key in col1:
        return col1.index(key), 1
    elif key in col2:
        return col2.index(key), 2


def row_col_directional_keypad(key):
    row0, row1 = "<v>", "x^A"
    if key in row0:
        return 0, row0.index(key)
    elif key in row1:
        return 1, row1.index(key)


def keypad_numeric(current_key, target_key):
    keys = [""]
    row_current, col_current = row_col_numeric_keypad(current_key)
    row_target, col_target = row_col_numeric_keypad(target_key)
    if col_current < col_target:
        keys[0] += ">" * (col_target - col_current)
    elif col_current > col_target and not (col_target == 0 and row_current == 0):
        keys[0] += "<" * (col_current - col_target)
    if row_current < row_target:
        if keys[0] != "":
            keys.append("^" * (row_target - row_current) + keys[0])
        keys[0] += "^" * (row_target - row_current)
    elif row_current > row_target:
        if keys[0] != "" and not (col_current == 0 and row_target == 0):
            keys.append("v" * (row_current - row_target) + keys[0])
        keys[0] += "v" * (row_current - row_target)
    if col_current > col_target and (col_target == 0 and row_current == 0):
        keys[0] += "<" * (col_current - col_target)
    return keys

def keypad_directional(current_key, target_key):
    keys = ""
    row_current, col_current = row_col_directional_keypad(current_key)
    row_target, col_target = row_col_directional_keypad(target_key)
    if col_current == col_target:
        if row_current < row_target:
            keys = "^"
        elif row_current > row_target:
            keys = "v"
    elif row_current == row_target:
        if col_current < col_target:
            keys = ">" * (col_target - col_current)
        elif col_current > col_target:
            keys = "<" * (col_current - col_target)
    else:
        if current_key == "<":
            if target_key == "^":
                keys = ">^"
            elif target_key == "A":
                keys = ">>^"
        elif target_key == "<":
            if current_key == "^":
                keys = "v<"
            elif current_key == "A":
                keys = "v<<"
        elif current_key == "^" and target_key == ">":
            keys = "v>"
        elif current_key == ">" and target_key == "^":
            keys = "<^"
        elif current_key == "A" and target_key == "v":
            keys = "<v"
        elif current_key == "v" and target_key == "A":
            keys = "^>"
    return keys

def numeric_to_directional(code):
    prev_key = "A"
    sequences = [""]
    for key in code:
        next_sequences = []
        for seq in sequences:
            for s in keypad_numeric(prev_key, key):
                next_sequences.append(seq + s + "A")
        prev_key = key
        sequences = next_sequences
    len_seq = min([len(s) for s in sequences])
    sequences = [s for s in sequences if len(s) == len_seq]
    return sequences


def sequence_to_counts(sequence):
    counts = {}
    prev_key = sequence[0]
    for key in sequence[1:]:
        doublet = prev_key + key
        if doublet in counts.keys():
            counts[doublet] += 1
        else:
            counts[doublet] = 1
        prev_key = key
    return counts

def directional_to_directional_counts(counts, start):
    start_doublet = "A" + start
    if start_doublet in counts.keys():
        counts[start_doublet] += 1
    else:
        counts[start_doublet] = 1
    counts_out = {}
    start_out = keypad_directional("A", start)[0]
    for doublet in counts.keys():
        sequence = keypad_directional(doublet[0], doublet[1])
        if sequence:
            prev_key = "A"
            for key in sequence:
                d = prev_key + key
                if d in counts_out.keys():
                    counts_out[d] += counts[doublet]
                else:
                    counts_out[d] = counts[doublet]
                prev_key = key
            d = sequence[-1] + "A"
        else:
            d = "AA"
        if d in counts_out.keys():
            counts_out[d] += counts[doublet]
        else:
            counts_out[d] = counts[doublet]
    counts_out["A" + start_out] -= 1
    return counts_out, start_out

f = open("input21.txt", "r")
codes = []
s = 0
for line in f:
    code = line.strip()
    codes.append(code)
    sequences = numeric_to_directional(code)
    min_seq_len = float('inf')
    for sequence in sequences:
        counts_temp = sequence_to_counts(sequence)
        start = sequence[0]
        for i in range(25):
            counts_temp, start = directional_to_directional_counts(counts_temp, start)
        seq_len = sum(counts_temp.values()) + 1
        if seq_len < min_seq_len:
            min_seq_len = seq_len
    s += min_seq_len * int(code[:-1])
print(s)







