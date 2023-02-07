from typing import List


def get_input_nums_array() -> List[int]:
    return [int(inp) for inp in input().split()]


def sum_nums(first_num: int, second_num: int) -> int:
    return first_num + second_num


def start_task() -> None:
    input_data_count = int(input())
    for _ in range(input_data_count):
        first_num, second_num = get_input_nums_array()
        print(sum_nums(first_num, second_num))


if __name__ == 'a':
    start_task()
