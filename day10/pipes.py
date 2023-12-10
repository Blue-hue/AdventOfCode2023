from collections import deque

with open("day10\input.txt") as f:
    s = f.read().splitlines()

for r, row in enumerate(s):
    for c, ch in enumerate(row):
        if ch == "S":
            sr = r
            sc = c
            break
    else:
        continue
    break

loop = {(sr, sc)}
q = deque([(sr, sc)])

while q:
    r, c = q.popleft()
    ch = s[r][c]

    if r > 0 and ch in "S|JL" and s[r - 1][c] in "|7F" and (r - 1, c) not in loop:
        loop.add((r - 1, c))
        q.append((r - 1, c))
        
    if r < len(s) - 1 and ch in "S|7F" and s[r + 1][c] in "|JL" and (r + 1, c) not in loop:
        loop.add((r + 1, c))
        q.append((r + 1, c))

    if c > 0 and ch in "S-J7" and s[r][c - 1] in "-LF" and (r, c - 1) not in loop:
        loop.add((r, c - 1))
        q.append((r, c - 1))

    if c < len(s[r]) - 1 and ch in "S-LF" and s[r][c + 1] in "-J7" and (r, c + 1) not in loop:
        loop.add((r, c + 1))
        q.append((r, c + 1))

print(len(loop) // 2)