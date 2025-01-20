def get_input():
    with open("input.txt") as f:
        data = f.read()
        data_splitted = data.split("\n")
        data_dict = {}
        for row in data_splitted:
            total, numbers = row.split(": ")
            numbers = numbers.split(" ")
            numbers = [int(x) for x in numbers]
            data_dict[total] = numbers
    return data_dict


def count(nums, target, concat=False):
    if len(nums) == 1:
        return nums[0] == target

    if concat:
        return (count([nums[0] + nums[1]] + nums[2:], target, True) +
                count([nums[0] * nums[1]] + nums[2:], target, True) +
                count([int(str(nums[0]) + str(nums[1]))] + nums[2:], target, True))

    return (count([nums[0] + nums[1]] + nums[2:], target) +
            count([nums[0] * nums[1]] + nums[2:], target))


def part1(data):
    total_sum = 0
    for total, numbers in data.items():
        # Check for all the possible combinations of operators
        target = int(total)
        if count(numbers, target):
            total_sum += target

    print(total_sum)


def part2(data):
    total_sum = 0
    for total, numbers in data.items():
        # Check for all the possible combinations of operators
        target = int(total)
        if count(numbers, target, True):
            total_sum += target

    print(total_sum)


if __name__ == "__main__":
    data = get_input()
    part1(data)
    part2(data)
