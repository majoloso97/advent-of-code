def get_input(filepath):
    a = []
    b = []
    with open(filepath) as f:
        for line in f:
            i, j = line.split("   ")
            a.append(int(i))
            b.append(int(j))
    return a, b


def distance(a, counter):
    return a * counter.get(a, 0)


a, b = get_input("input.txt")

a_vals = set(a)
counter = dict.fromkeys(a_vals, 0)

for value in b:
    if value in counter:
        counter[value] += 1

distances = map(lambda x: distance(x, counter), a)
print(sum(distances))
