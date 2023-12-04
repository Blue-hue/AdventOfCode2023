with open("day1\input.txt") as f:
    s = f.read()
summ = 0
for word in s.strip().split("\n"):
    digits = []
    for i, letter in enumerate(word):
        if letter.isdigit():
            digits.append(letter)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if word[i:].startswith(val):
                digits.append(str(d+1))
    score = int(digits[0] + digits[-1])
    summ += score
print(summ)
