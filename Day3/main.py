import re


def get_input():
    with open("input.txt") as f:
        data = f.read()
        return data


def part1():
    data = get_input()
    regex = r"mul\((\d+),(\d+)\)"
    matches = re.findall(regex, data)
    total = 0

    for n1, n2 in matches:
        total += int(n1) * int(n2)

    print(total)


def part2():
    data = get_input()
    regex = r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))"
    matches = re.findall(regex, data)
    total = 0

    # Default to multiple
    mul = True

    for n1, n2, do, dont in matches:
        if do:
            mul = True
            continue
        elif dont:
            mul = False
            continue

        if mul:
            total += int(n1) * int(n2)

    print(total)


if __name__ == '__main__':
    part1()
    part2()
