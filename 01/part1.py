import re

puzzle = open('input.txt').read()
puzzle = puzzle.split('\n')

total = 0

for line in puzzle:
    nums = re.findall(r"\d", line)
    total += (int(nums[0]) * 10) + int(nums[-1])

print(total)
