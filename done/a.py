from typing import List

input_data_count = int(input())


def get_input_nums_array() -> List[int]:
    return [int(inp) for inp in input().split()]


def start_task() -> None:
    for _ in range(input_data_count):
        first_num, second_num = get_input_nums_array()
        print(first_num + second_num)


start_task()
