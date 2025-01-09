# f = open("input1.txt", "r")
# s = 0
# for line in f:
#     digits = [int(char) for char in list(line) if char.isdigit()]
#     s += digits[0] * 10 + digits[-1]
#
# print(s)

f = open("input1.txt", "r")
s = 0
valid_digits = {'one': 'one1one', 'two': 'two2two', 'three': 'three3three', 'four': 'four4four', 'five': 'five5five',
                'six': 'six6six', 'seven': 'seven7seven', 'eight': 'eight8eight', 'nine': 'nine9nine'}
for line in f:
    line_rep = line
    for key in valid_digits:
        line_rep = line_rep.replace(key, valid_digits[key])
    digits = [int(char) for char in list(line_rep) if char.isdigit()]
    s += digits[0] * 10 + digits[-1]

print(s)





