import re


def get_input():
    with open("input.txt") as f:
        data = f.read()
        return data


def part1():
    data = get_input()
    regex = r"XMAS"
    regex_rev = r"SAMX"
    data_lines = data.split('\n')

    matches_horizontal = re.findall(regex, data)
    matches_horizontal_reversed = re.findall(regex_rev, data)

    vertical_lines = []

    for i in range(len(data_lines[0])):
        vertical_lines.append(''.join([data_lines[j][i] for j in range(len(data_lines))]))

    matches_vertical = re.findall(regex, '\n'.join(vertical_lines))
    matches_vertical_reversed = re.findall(regex, '\n'.join([line[::-1] for line in vertical_lines]))

    diagonal_length = len(data_lines)

    diagonal_falling = []
    for row in reversed(range(diagonal_length)):
        line = ""
        for i in range(row, diagonal_length):
            line += data_lines[i][i - row]
        diagonal_falling.append(line)

    for column in range(1, diagonal_length):  # 0-9
        line = ""
        for i in range(0, diagonal_length - column):  # 0-9
            line += data_lines[i][i + column]
        diagonal_falling.append(line)

    diagonal_rising = []

    for row in range(diagonal_length):
        line = ""
        for i in range(row + 1):
            line += data_lines[row - i][i]
        diagonal_rising.append(line)

    for column in range(1, diagonal_length):
        line = ""
        for i in range(diagonal_length - column):
            line += data_lines[diagonal_length - 1 - i][column + i]
        diagonal_rising.append(line)

    matches_diagonal_r = re.findall(regex, '\n'.join(diagonal_rising))
    matches_diagonal_f = re.findall(regex, '\n'.join(diagonal_falling))
    matches_diagonal_f_reversed = re.findall(regex, '\n'.join([line[::-1] for line in diagonal_falling]))
    matches_diagonal_r_reversed = re.findall(regex, '\n'.join([line[::-1] for line in diagonal_rising]))

    total_matches = (
            len(matches_horizontal) +
            len(matches_horizontal_reversed) +
            len(matches_vertical) +
            len(matches_vertical_reversed) +
            len(matches_diagonal_f) +
            len(matches_diagonal_r) +
            len(matches_diagonal_f_reversed) +
            len(matches_diagonal_r_reversed)
    )

    print(total_matches)


def part2():
    data = get_input()
    split_data = data.split('\n')

    def check_x(row, column):
        x_right = (split_data[row - 1][column - 1] + split_data[row][column] + split_data[row + 1][column + 1])
        x_left = (split_data[row - 1][column + 1] + split_data[row][column] + split_data[row + 1][column - 1])

        if (x_right == 'MAS' or x_right == 'SAM') and (x_left == 'MAS' or x_left == 'SAM'):
            return True

        return False

    x_counter = 0
    for row in range(1, len(split_data) - 1):
        for column in range(1, len(split_data[row]) - 1):
            if split_data[row][column] == 'A':
                if check_x(row, column):
                    x_counter += 1

    print(x_counter)


if __name__ == '__main__':
    part1()
    part2()
