from typing import List

MAX_LEVEL = 100


def find_coproger(couples_list: List[int], couples_count: int) -> List[List]:
    res = []
    for proger_index in range(couples_count):

        current_proger = couples_list[proger_index]

        if current_proger > MAX_LEVEL:
            continue

        abs_levels_list = [abs(i - current_proger) for i in couples_list]
        min_level_dif = min(abs_levels_list[proger_index + 1:])
        coproger_index = abs_levels_list.index(min_level_dif, proger_index + 1)

        couples_list[coproger_index] = couples_list[coproger_index] + (MAX_LEVEL * 10)

        res.append([proger_index + 1, coproger_index + 1])
    return res


def get_input_nums_array() -> List[int]:
    return [int(inp) for inp in input().split()]


def start_task() -> None:
    iters_num = int(input())  # 1

    for _ in range(iters_num):
        progers_count = int(input())  # 6
        progers_levels = get_input_nums_array()  # [2, 1, 3, 1, 1, 4]
        for couple in find_coproger(progers_levels, progers_count):
            print(couple[0], couple[1])


start_task()
