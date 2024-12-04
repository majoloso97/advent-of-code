def is_xmas(substr=""):
    if substr == "XMAS":
        return True
    return False


def right(input, row, col, rows, cols):
    if cols - col < 4:
        return ""
    substr = input[row][col : col + 4]
    return substr


def left(input, row, col, rows, cols):
    if col < 3:
        return ""
    substr = input[row][col - 3 : col + 1][::-1]
    return substr


def top(input, row, col, rows, cols):
    if row < 3:
        return ""
    substr = (
        input[row][col]
        + input[row - 1][col]
        + input[row - 2][col]
        + input[row - 3][col]
    )
    return substr


def bottom(input, row, col, rows, cols):
    if rows - row < 4:
        return ""
    substr = (
        input[row][col]
        + input[row + 1][col]
        + input[row + 2][col]
        + input[row + 3][col]
    )
    return substr


def top_right(input, row, col, rows, cols):
    if (row < 3) or (cols - col < 4):
        return ""
    substr = (
        input[row][col]
        + input[row - 1][col + 1]
        + input[row - 2][col + 2]
        + input[row - 3][col + 3]
    )
    return substr


def top_left(input, row, col, rows, cols):
    if (row < 3) or (col < 3):
        return ""
    substr = (
        input[row][col]
        + input[row - 1][col - 1]
        + input[row - 2][col - 2]
        + input[row - 3][col - 3]
    )
    return substr


def bottom_right(input, row, col, rows, cols):
    if (rows - row < 4) or (cols - col < 4):
        return ""
    substr = (
        input[row][col]
        + input[row + 1][col + 1]
        + input[row + 2][col + 2]
        + input[row + 3][col + 3]
    )
    return substr


def bottom_left(input, row, col, rows, cols):
    if (rows - row < 4) or (col < 3):
        return ""
    substr = (
        input[row][col]
        + input[row + 1][col - 1]
        + input[row + 2][col - 2]
        + input[row + 3][col - 3]
    )
    return substr


def get_input(filepath):
    lines = []
    with open(filepath) as f:
        for line in f:
            lines.append(line)
    return lines


input = get_input("input.txt")

counter = 0
funcs = [
    right,
    left,
    top,
    bottom,
    top_right,
    top_left,
    bottom_right,
    bottom_left,
]
rows = len(input)
for row in range(rows):
    cols = len(input[row])
    for col in range(cols):
        if input[row][col] != "X":
            continue
        for f in funcs:
            substr = f(input, row, col, rows, cols)
            if is_xmas(substr):
                counter += 1

print(counter)
