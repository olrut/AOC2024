def get_input():
    with open("input.txt") as f:
        data = f.read()
    return data


def disk_map(data):
    total = []
    for i in range(0, len(data), 2):
        multiplier = int(data[i])
        if i + 1 < len(data):
            space = int(data[i + 1])
        else:
            space = 0
        for _ in range(int(multiplier)):
            total.append(str(i // 2))
        for _ in range(int(space)):
            total.append(".")
    return total


def part1(data):
    total = disk_map(data)
    total_rev = [i for i in total[::-1] if i != "."]

    end_counter = 0
    for i in range(0, len(total)):
        if total[i] == ".":
            total[i] = total_rev[0]
            end_counter -= 1
            total_rev = total_rev[1:]
    total = total[:end_counter]

    total_sum = 0
    for i in range(0, len(total)):
        total_sum += int(total[i]) * i

    print(total_sum)


def part2(data):
    total = disk_map(data)

    i_from_end = len(total) - 1

    while i_from_end > 0:
        file_length = 0
        file_num = total[i_from_end]
        if file_num == ".":
            i_from_end -= 1
            continue

        while total[i_from_end] == file_num:
            file_length += 1
            i_from_end -= 1

        for i in range(len(total)):
            if total[i] == ".":
                start_i = i
                stop_i = i
                while total[stop_i] == ".":
                    stop_i += 1
                    if stop_i == len(total):
                        break
                if stop_i - start_i >= file_length:
                    k = i_from_end + 1
                    if start_i > k:
                        break
                    for j in range(start_i, start_i + file_length):
                        total[j] = file_num
                        total[k] = "x"
                        k += 1
                    break

    total_sum = 0
    for i in range(0, len(total)):
        if total[i] != "." and total[i] != "x":
            total_sum += int(total[i]) * i

    print("".join(total))

    print(total_sum)


if __name__ == "__main__":
    data = get_input()
    part1(data)
    part2(data)
