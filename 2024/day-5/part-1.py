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


def parse_input(raw_input):
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
    return order_rules, pages


input = get_input("input.txt")
order_rules, pages = parse_input(input)
ordered = []
unordered = []
for page in pages:
    page_len = len(page)
    is_ordered = True
    for i in range(page_len):
        rule = order_rules.get(page[i])
        if not rule:
            continue
        for k in range(i):
            if page[k] in rule:
                is_ordered = False
                break
        if not is_ordered:
            break
    if is_ordered:
        ordered.append(page)
    else:
        unordered.append(page)

total = 0
for page in ordered:
    if len(page) % 2 == 0:
        break
    position = int((len(page) + 1) / 2) - 1
    total += page[position]
print(total)
