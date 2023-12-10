import math
with open("day8\input.txt") as f:
    s = f.read()

steps, *paths = s.split('\n')
path_dict = dict()
for path in paths:
    source, dest = path.split(' = ')
    dest = dest.replace('(','').replace(')','').replace(' ','').split(',')
    path_dict[source] = dest

def find_z(location):
    count = 0
    stepnum = 0
    #while location != 'ZZZ':   #----->PART1
    while location[-1] != 'Z': 
        location = path_dict[location][0 if steps[stepnum % len(steps)] == 'L' else 1]
        count += 1
        stepnum += 1
    return count

print(find_z('AAA'))

locations = []
for step in path_dict.keys():
    if step[-1]=='A':
        locations.append(step)
print(locations)

needed = []
for location in locations:

    needed.append(find_z(location))
print(needed)

ans = needed[0]
for num in needed:
    ans = ans * num // math.gcd(ans, num)
print(ans)
