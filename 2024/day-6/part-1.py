def get_input(filename, guards):
    lines = []
    position = (0, 0)
    current_ln = 0
    guard = "^"
    with open(filename) as f:
        for ln in f:
            line = ln.replace("\n", "")
            line_len = len(line)
            for i in range(line_len):
                if line[i] in guards:
                    position = (current_ln, i)
                    guard = line[i]
            lines.append(line)
            current_ln += 1
    return lines, position, guard


def move_up(input, x, y):
    if input[x - 1][y] == "#":
        return (x, y), ">"
    return (x - 1, y), "^"


def move_down(input, x, y):
    if input[x + 1][y] == "#":
        return (x, y), "<"
    return (x + 1, y), "v"


def move_left(input, x, y):
    if input[x][y - 1] == "#":
        return (x, y), "^"
    return (x, y - 1), "<"


def move_right(input, x, y):
    if input[x][y + 1] == "#":
        return (x, y), "v"
    return (x, y + 1), ">"


def get_next_position(input, guard_position, guard, guards):
    func = guards.get(guard)
    next_position, next_guard = func(input, *guard_position)
    return next_position, next_guard


guards = {
    "^": move_up,
    ">": move_right,
    "v": move_down,
    "<": move_left,
}
visited_positions = set()
input, guard_position, guard = get_input("input.txt", guards.keys())
visited_positions.add(guard_position)
height = len(input)
width = len(input[0])


while True:
    if (
        (guard_position[0] - 1 < 0)
        or (guard_position[1] - 1 < 0)
        or (guard_position[0] + 1 >= height)
        or (guard_position[1] + 1 >= width)
    ):
        break
    guard_position, guard = get_next_position(input, guard_position, guard, guards)
    visited_positions.add(guard_position)

print(len(visited_positions))
