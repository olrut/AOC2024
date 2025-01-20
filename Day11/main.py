import functools
import math


def get_input():
    with open("input.txt") as f:
        data = f.read().split(" ")
        for i in range(len(data)):
            data[i] = int(data[i])
        return data


@functools.cache
def check_int_digits(num):
    if num <= 999999999999997:
        digit_len = int(math.log10(num)) + 1
        return digit_len % 2 == 0
    else:
        return len(str(num)) % 2 == 0


@functools.cache
def year_multiply(num):
    return num * 2024


@functools.cache
def blink(num, times, stones):
    if times == 0:
        return stones
    if num == 0:
        return blink(1, times - 1, stones)

    if check_int_digits(num):
        str_i = str(num)
        i_halved1 = str_i[:len(str_i) // 2]
        i_halved2 = str_i[len(str_i) // 2:]
        return blink(int(i_halved1), times - 1, stones) + blink(int(i_halved2), times - 1, stones)
    else:
        return blink(year_multiply(num), times - 1, stones)


def part1(data):
    counter = 0
    for num in data:
        counter += blink(num, 25, 1)
    print(counter)


def part2(data):
    counter = 0
    for num in data:
        counter += blink(num, 75, 1)
    print(counter)


if __name__ == "__main__":
    data = get_input()
    part1(data)
    part2(data)
