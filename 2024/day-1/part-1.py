def get_input(filepath):
    a = []
    b = []
    with open(filepath) as f:
        for line in f:
            i, j = line.split("   ")
            a.append(int(i))
            b.append(int(j))
    return a, b


def distance(a, b):
    return abs(a - b)


a, b = get_input("input.txt")

a.sort()
b.sort()

distances = map(lambda x: distance(*x), zip(a, b))
print(sum(distances))
