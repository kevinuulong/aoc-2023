import re

puzzle = open('input.txt').read()
puzzle = puzzle.split('\n')

total = 0

for game in puzzle:
    draws = re.sub(r"Game (\d*): ", "", game).split("; ")
    reds = []
    blues = []
    greens = []
    for draw in draws:
        red = blue = green = 0
        try:
            red = int(re.search(r"(\d*) red", draw).group(1))
        except:
            pass
        try:
            blue = int(re.search(r"(\d*) blue", draw).group(1))
        except:
            pass
        try:
            green = int(re.search(r"(\d*) green", draw).group(1))
        except:
            pass
        
        reds.append(red)
        blues.append(blue)
        greens.append(green)

    total += max(reds) * max(blues) * max(greens)

print(total)