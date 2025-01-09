# f = open("input17.txt", "r")
#
# for line in f:
#     line_split = line.split()
#     if "Register A" in line:
#         regA = int(line_split[-1])
#     if "Register B" in line:
#         regB = int(line_split[-1])
#     if "Register C" in line:
#         regC = int(line_split[-1])
#     if "Program" in line:
#         program = line_split[-1]
#         program = [int(ch) for ch in program.split(",")]
#
#
# def combo_operand(operand, regA, regB, regC):
#     out = operand
#     if operand == 4:
#         out = regA
#     elif operand == 5:
#         out = regB
#     elif operand == 6:
#         out = regC
#     elif operand >= 7:
#         print("Error")
#     return out
#
#
# def op(instruction, operand, regA, regB, regC):
#     pointer = None
#     out = ""
#     if instruction == 1:
#         regB = operand ^ regB
#     elif instruction == 3:
#         if regA != 0:
#             pointer = operand
#     else:
#         operand = combo_operand(operand, regA, regB, regC)
#         if instruction == 0:
#             regA = regA // 2 ** operand
#         elif instruction == 2:
#             regB = operand % 8
#         elif instruction == 4:
#             regB = regB ^ regC
#         elif instruction == 5:
#             out = operand % 8
#         elif instruction == 6:
#             regB = regA // 2 ** operand
#         elif instruction == 7:
#             regC = regA // 2 ** operand
#     return out, pointer, regA, regB, regC
#
# pointer = 0
# outputs = ""
# while pointer < len(program):
#     out, p, regA, regB, regC = op(program[pointer], program[pointer + 1], regA, regB, regC)
#     outputs += str(out)
#     if p is None:
#         pointer += 2
#     else:
#         pointer = p
#
# print(outputs)
import numpy as np
from fontTools.unicodedata import block

f = open("input17.txt", "r")

for line in f:
    line_split = line.split()
    if "Register A" in line:
        regA = int(line_split[-1])
    if "Register B" in line:
        regB = int(line_split[-1])
    if "Register C" in line:
        regC = int(line_split[-1])
    if "Program" in line:
        program = line_split[-1]
        program_str = program.replace(",", "")
        program = [int(ch) for ch in program.split(",")]


def combo_operand(operand, regA, regB, regC):
    out = operand
    if operand == 4:
        out = regA
    elif operand == 5:
        out = regB
    elif operand == 6:
        out = regC
    elif operand >= 7:
        print("Error")
    return out


def op(instruction, operand, regA, regB, regC):
    pointer = None
    out = ""
    if instruction == 1:
        regB = operand ^ regB
    elif instruction == 3:
        if regA != 0:
            pointer = operand
    else:
        operand = combo_operand(operand, regA, regB, regC)
        if instruction == 0:
            regA = regA // 2 ** operand
        elif instruction == 2:
            regB = operand % 8
        elif instruction == 4:
            regB = regB ^ regC
        elif instruction == 5:
            out = operand % 8
        elif instruction == 6:
            regB = regA // 2 ** operand
        elif instruction == 7:
            regC = regA // 2 ** operand
    return out, pointer, regA, regB, regC


def run_program(regA, regB, regC):
    pointer = 0
    outputs = ""
    while pointer < len(program):
        out, p, regA, regB, regC = op(program[pointer], program[pointer + 1], regA, regB, regC)
        outputs += str(out)
        if p is None:
            pointer += 2
        else:
            pointer = p
    return outputs

regA_init, regB_init, regC_init = int(3e13), regB, regC

regA_init = int(265652340990875)

block_len_expo = 14

regA = regA_init
possible_values = []
outputs_list = []
while True:
    outputs = run_program(regA, regB_init, regC_init)
    if outputs == program_str:
        break
    if len(outputs) > 16:
        break
    outputs_list.append(outputs)
    if outputs[-block_len_expo:] == program_str[-block_len_expo:]:
        possible_values.append(regA)
    regA += 10 ** int(14 - block_len_expo)

print(regA)
