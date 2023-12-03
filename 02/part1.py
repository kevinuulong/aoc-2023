import re

puzzle = open('input.txt').read()
puzzle = puzzle.split('\n')

bag = {'red': 12, 'green': 13, 'blue': 14}

total = 0

for i, game in enumerate(puzzle):
    draws = re.sub(r"Game (\d*): ", "", game).split("; ")
    valid = True
    for draw in draws:
        # colors = re.finditer(r"(((?P<blue>\d*) blue)|((?P<red>\d*) red)|((?P<green>\d*) green))", draw)
        try:
            red = int(re.search(r"(\d*) red", draw).group(1))
        except:
            red = 0
        try:
            green = int(re.search(r"(\d*) green", draw).group(1))
        except:
            green = 0
        try:
            blue = int(re.search(r"(\d*) blue", draw).group(1))
        except:
            blue = 0
        if (red > bag['red'] or blue > bag['blue'] or green > bag['green']):
            valid = False
            break
    total += (i + 1) if valid else 0

print(total)