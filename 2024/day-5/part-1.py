def get_input(filepath):
    lines = []
    with open(filepath) as f:
        for line in f:
            lines.append(line)
    return lines


def add_rule(rules, new_rule):
    a, b = map(int, new_rule.split("|"))
    if a in rules:
        rules[a].append(b)
    else:
        rules[a] = [b]
    return rules


input = get_input("input.txt")
order_rules = {}
pages = []

split_flag = False
for l in input:
    l = l.replace("\n", "")
    if l == "":
        split_flag = not split_flag
        continue
    if split_flag:
        pages.append(list(map(int, l.split(","))))
    else:
        add_rule(order_rules, l)
print(order_rules)
print(pages)
