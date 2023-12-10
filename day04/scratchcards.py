from collections import defaultdict
with open("day4\input.txt") as f:
    s = f.read()
ans = 0
n = defaultdict(int)

for i, line in enumerate(s.split('\n')):
    n[i] += 1
    matches = 0
    wins = [int(i) for i in line.split(':')[1].split('|')[0].split()]
    mine = [int(i) for i in line.split(':')[1].split('|')[1].split()]
    for card in wins:
        if card in mine:
            matches += 1
    if matches >= 1:
        ans += 2**(matches-1)
    for j in range(matches):
        n[j+1+i] += n[i]

print(sum(n.values()))
print(ans)



