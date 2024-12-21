def get_first_digit(line):
    for c in line:
        if c.isnumeric():
            return int(c)


total = 0
filename = "input.txt"

with open(filename) as f:
    first = 0
    last = 0
    for line in f:
        first = get_first_digit(line)
        last = get_first_digit(line[::-1])
        value = (first * 10) + last
        total += value

print(total)
