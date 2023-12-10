with open("day9\input.txt") as f:
    s = f.read().strip().splitlines()
ans1 = 0
ans2 = 0
def extrapolate(line, part2):
    diff = [b-a for a,b in zip(line, line[1:])]
    if all(num==0 for num in diff):
        return line[-1 if not part2 else 0]
    else:                   
        return line[-1 if not part2 else 0] + (1 if not part2 else -1) * extrapolate(diff, part2)

for line in s:
    line = [int(x) for x in line.split()]
    ans1 += extrapolate(line, False)
    ans2 += extrapolate(line, True)

print(ans1, ans2)
