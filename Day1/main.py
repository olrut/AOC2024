def get_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
        list1 = [x.split("   ")[0] for x in data]
        list1.sort()
        list2 = [x.split("   ")[1] for x in data]
        list2.sort()
        return list1, list2


def part1():
    list1, list2 = get_input()

    distance = 0
    for i in range(len(list1)):
        distance += abs(int(list1[i]) - int(list2[i]))

    print(distance)


def part2():
    list1, list2 = get_input()

    similarity_score = 0

    for i in range(len(list1)):
        count = list2.count(list1[i])
        if count > 0:
            similarity_score += count * int(list1[i])

    print(similarity_score)


if __name__ == '__main__':
    part1()
    part2()
