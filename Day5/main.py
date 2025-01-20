from collections import defaultdict


def get_input():
    with open("input.txt") as f:
        data = f.read()
        rules = data.split("\n\n")[0].split("\n")
        rules = [x.split("|") for x in rules]
        rules_dict = defaultdict(list)

        for r_num1, r_num2 in rules:
            rules_dict[int(r_num1)].append(int(r_num2))

        updates = data.split("\n\n")[1].split("\n")
        updates = [x.split(",") for x in updates]
        updates = [[int(i) for i in x] for x in updates]

        return rules_dict, updates


def part1(rules_dict, updates):
    total = 0

    invalid_pages = []

    for page in updates:
        valid_page = True

        for page_num in page:
            if page_num not in rules_dict:
                continue

            rules = rules_dict[page_num]
            for rule in rules:
                if rule in page:
                    r_index = page.index(rule)
                    p_num_index = page.index(page_num)
                    if r_index < p_num_index:
                        valid_page = False
                        break

        if valid_page:
            total += page[len(page) // 2]
        else:
            invalid_pages.append(page)

    print(total)
    return invalid_pages


def part2(rules_dict, invalid):
    total = 0

    def fix(arr, arr_rules):
        arr_copy = arr.copy()  # Copy of the input array
        topological_order = []  # Store topological order

        while len(topological_order) < len(arr):
            for current in arr_copy:
                if current in topological_order:
                    continue

                should_be_after = []

                for r in arr_rules:
                    ruls = arr_rules[r]
                    for rul in ruls:
                        if rul == current and rul in arr_copy:
                            should_be_after.append(r)

                if all([x in topological_order for x in should_be_after]):
                    topological_order.append(current)
                    arr_copy.remove(current)

        return topological_order

    for p in invalid:
        related_rules = {}
        for page_num in p:
            if page_num in rules_dict:
                related_rules[page_num] = rules_dict[page_num]

        fixed_page = fix(p, related_rules)

        total += fixed_page[len(fixed_page) // 2]

    print(total)


if __name__ == "__main__":
    rules_dict, updates = get_input()
    invalid_pages = part1(rules_dict, updates)
    part2(rules_dict, invalid_pages)
