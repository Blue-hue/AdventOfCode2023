import re
with open("day2\input.txt") as f:
    s = f.read()
summ = 0
red_p = "(\d+) red"
blue_p = "(\d+) blue"
green_p = "(\d+) green"
game = "Game (\d+)"
prod = 0

for line in s.strip().split('\n'):
    flag = 1
    red_match = [int(i) for i in re.findall(red_p, line)]
    green_match = [int(i) for i in re.findall(green_p, line)]
    blue_match = [int(i) for i in re.findall(blue_p, line)]
    game_num = int(re.findall(game, line)[0])

    for num in red_match:
        if num > 12:
            flag = 0
    for num in green_match:
        if num > 13:
            flag = 0
    for num in blue_match:
        if num > 14:
            flag = 0
    if flag:
        summ += game_num
    
    red = max(red_match)
    blue = max(blue_match)
    green = max(green_match)
    prod = prod + (red * blue * green)
print(summ)

print(prod)



   





max = {'red':12, 'green':13, 'blue':14}


