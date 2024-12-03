import re

with open("input.txt") as f:
    memory = f.read()

enabled = True
result = 0

for instr in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", memory):
    if instr == "do()":
        enabled = True
    elif instr == "don't()":
        enabled = False
    elif enabled:
        x, y = map(int, re.findall(r"\d+", instr))
        result += x * y

print(result)
