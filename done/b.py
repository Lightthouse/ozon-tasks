from collections import Counter
from typing import List


def products_sum(input_list: List[int]) -> int:
    list_sum = 0
    counted_list = Counter(input_list)
    for price in counted_list:
        list_sum += int(price) * (counted_list[price] - counted_list[price] // 3)
    return list_sum


def get_input_nums_array() -> List[int]:
    return [int(inp) for inp in input().split()]


def start_task() -> None:
    iters_num = int(input())
    for _ in range(iters_num):
        int(input())  # input_length
        input_numbers = get_input_nums_array()

        print(products_sum(input_numbers))


start_task()
