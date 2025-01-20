def get_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
        data_split = [list(map(int, x.split())) for x in data]
        return data_split


def check_adjacent(int_list, is_increasing, dampener=False, dampener_score=0):
    # Check if the list is valid according to the rules
    def is_invalid(current_num, next_num):
        difference = abs(current_num - next_num)
        if is_increasing:
            adjacent = current_num >= next_num
        else:
            adjacent = current_num <= next_num
        return difference > 3 or difference == 0 or adjacent

    for i in range(len(int_list) - 1):
        if is_invalid(int_list[i], int_list[i + 1]):
            if dampener and dampener_score < 1:
                list_without_current = int_list[:i] + int_list[i + 1:]
                list_without_next = int_list[:i + 1] + int_list[i + 2:]
                return check_adjacent(list_without_current, is_increasing, True,
                                      dampener_score + 1) or check_adjacent(list_without_next, is_increasing, True,
                                                                            dampener_score + 1)
            return False

    return True


def part1():
    data = get_input()
    safe_counter = 0

    for i in range(len(data)):
        if check_adjacent(data[i], True) or check_adjacent(data[i], False):
            safe_counter += 1

    return safe_counter


def part2():
    data = get_input()
    safe_counter = 0

    for i in range(len(data)):
        if check_adjacent(data[i], True, True) or check_adjacent(data[i], False, True):
            safe_counter += 1
            
    return safe_counter


if __name__ == '__main__':
    print(part1())
    print(part2())
