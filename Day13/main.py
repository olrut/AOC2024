from dataclasses import dataclass


@dataclass
class Data:
    prize: tuple
    button_a: tuple
    button_b: tuple


def get_input():
    with open("input.txt") as f:
        data = f.read().split("\n\n")
        data_dict = {}
        for i in range(len(data)):
            lines = data[i].splitlines()
            button_a = lines[0].split("Button A: ")[1]
            button_a = button_a.replace("X+", "")
            button_a = button_a.replace("Y+", "")
            button_a = button_a.split(", ")
            button_a = (int(button_a[0]), int(button_a[1]))

            button_b = lines[1].split("Button B: ")[1]
            button_b = button_b.replace("X+", "")
            button_b = button_b.replace("Y+", "")
            button_b = button_b.split(", ")
            button_b = (int(button_b[0]), int(button_b[1]))

            prize = lines[2].split("Prize: ")[1]
            prize = prize.replace("X=", "")
            prize = prize.replace("Y=", "")
            prize = prize.split(", ")
            prize = (int(prize[0]), int(prize[1]))

            data_dict[i] = Data(prize, button_a, button_b)

        return data_dict


def get_price(prize, button_a, button_b):
    total = 0
    tolerance = 0.01

    a = (button_b[0] * prize[1] - button_b[1] * prize[0]) / (button_b[0] * button_a[1] - button_b[1] * button_a[0])
    b = (prize[0] - button_a[0] * a) / button_b[0]
    if abs(a - round(a)) < tolerance and abs(b - round(b)) < tolerance:
        total += 3 * a + b

    return total


def part1(data):
    total = 0
    for i in range(len(data)):
        prize = data[i].prize
        button_a = data[i].button_a
        button_b = data[i].button_b
        prize = get_price(prize, button_a, button_b)
        total += prize
    print(total)


def part2(data):
    total = 0
    for i in range(len(data)):
        prize = data[i].prize
        prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)
        button_a = data[i].button_a
        button_b = data[i].button_b
        prize = get_price(prize, button_a, button_b)
        total += prize
    print(total)


if __name__ == "__main__":
    data = get_input()
    part1(data)
    part2(data)
