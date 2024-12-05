def is_xmas(input, row, col, rows, cols):
    if (row == 0) or (col == 0) or (rows - row == 1) or (cols - col == 1):
        return False

    downward = input[row - 1][col - 1] + "A" + input[row + 1][col + 1]
    upward = input[row - 1][col + 1] + "A" + input[row + 1][col - 1]

    # print(f"Position {row}, {col}. Downward: {downward} | Upward: {upward}")

    if (downward == "MAS" or downward == "SAM") and (
        upward == "MAS" or upward == "SAM"
    ):
        return True
    return False


def get_input(filepath):
    lines = []
    with open(filepath) as f:
        for line in f:
            lines.append(line)
    return lines


input = get_input("input.txt")

counter = 0
rows = len(input)
for row in range(rows):
    cols = len(input[row])
    for col in range(cols):
        if input[row][col] != "A":
            continue
        if is_xmas(input, row, col, rows, cols):
            counter += 1

print(counter)
