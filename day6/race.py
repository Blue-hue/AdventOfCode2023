with open("day6\input.txt") as f:
    s = f.read()
ans = 1
times = list(map(int, s.split('\n')[0].split(':')[1].split()))
dist = list(map(int, s.split('\n')[1].split(':')[1].split()))


'''     ===PART1===     '''

for i in range(len(times)):
    count = 0
    t = times[i]
    d = dist[i]
    for j in range(t):
        if j * (t - j) > d:
            count += 1
    ans *= count
print(ans)

'''     ===PART2===     '''

times = [str(i) for i in times]
dist = [str(i) for i in dist]
times = int("".join(times))
dist = int("".join(dist))
count = 0
for j in range(times):
        if j * (times - j) > dist:
            count += 1
print(count)

