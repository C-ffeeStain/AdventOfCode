ipt = []
with open("2023/day1_input.txt", "r") as f:
    ipt = f.readlines()


digits = []
last_digit = None
last_n = None
for n, line in enumerate(ipt):
    digits.append("")
    for n0, char in enumerate(line):
        if char.isdigit():
            digits[n] += char
            break
    for char1 in reversed(line[n0 + 1:]):
        if char1.isdigit() :
            digits[n] += char1
            break
    if len(digits[n]) == 1:
        digits[n] *= 2

total = 0
for num in digits:
    total += int(num)

print(total)