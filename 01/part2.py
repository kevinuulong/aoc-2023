import re
from helpers import str_to_int

puzzle = open('input.txt').read()
puzzle = puzzle.split('\n')

total = 0

for line in puzzle:
    nums = (re.search(r"\d|one|two|three|four|five|six|seven|eight|nine", line).group(0), re.search(r".*(\d|one|two|three|four|five|six|seven|eight|nine)", line).group(1))
    print(nums)
    total += (str_to_int(nums[0]) * 10) + str_to_int(nums[1])

print(total)