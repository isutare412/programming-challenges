# @JUDGE_ID: XXXXXX 100 Python "Dynamic Programming"

cycle_result = {}


def cycle_len(num: int):
    if num in cycle_result:
        return cycle_result[num]

    origin_num = num
    cycle = 1
    while num > 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        cycle += 1

    cycle_result[origin_num] = cycle
    return cycle


def find_largest_cycle(lhs: int, rhs: int):
    start = lhs < rhs and lhs or rhs
    end = lhs < rhs and rhs or lhs

    largest = 1
    for n in range(start, end+1):
        cycle = cycle_len(n)
        largest = largest < cycle and cycle or largest
    return largest


if __name__ == '__main__':
    from sys import stdin

    lines = stdin.read()
    for line in iter(lines.splitlines()):
        try:
            lhs, rhs = line.split()
        except ValueError:
            continue

        lhs = int(lhs)
        rhs = int(rhs)
        largest = find_largest_cycle(lhs, rhs)
        print('{} {} {}'.format(lhs, rhs, largest))
