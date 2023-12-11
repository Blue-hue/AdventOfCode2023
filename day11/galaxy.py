with open("day11\input.txt") as f:
    s = f.read().splitlines()

#replacement = 2        #-----------> PART1
replacement = 1000000   #-----------> PART2

ans = 0

points = [(r,c) for r,row in enumerate(s) for c,ch in enumerate(row) if ch == '#']

p_rows = set(point[0] for point in points)
p_cols = set(point[1] for point in points)

for i in range(len(points)-1):
    for j in range(i,len(points)):
        for k in range(min(points[i][0], points[j][0]), max(points[i][0], points[j][0])):
            ans += replacement if k not in p_rows else 1
        for k in range(min(points[i][1], points[j][1]), max(points[i][1], points[j][1])):
            ans += replacement if k not in p_cols else 1

print(ans)



