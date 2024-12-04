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


input = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]

counter = 0
funcs = [
    # right,
    # left,
    top,
    # bottom,
]
rows = len(input)
for row in range(rows):
    cols = len(input[row])
    for col in range(cols):
        if input[row][col] != "X":
            continue
        for f in funcs:
            substr = f(input, row, col, rows, cols)
            print(substr)
            if is_xmas(substr):
                counter += 1

print(counter)
