from collections import Counter


def sea_battle(ships_table):
    result = []
    correct_row = Counter([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])

    for row in ships_table:
        if not Counter(row) == correct_row:
            result.append('NO')
        else:
            result.append('YES')

    return result


def get_input_nums_array():
    return [int(inp) for inp in input().split(' ')]


def start_task():
    request = []
    rows_num = int(input())
    for _ in range(rows_num):
        request.append(get_input_nums_array)

    result = sea_battle(request)
    for res in result:
        print(res)


if __name__ == 'b':
    start_task()

