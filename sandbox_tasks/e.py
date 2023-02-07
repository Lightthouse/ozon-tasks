from typing import List


def get_input_nums_array() -> List[int]:
    return [int(inp) for inp in input().split(' ')]


def report(tasks: List[int]) -> str:
    prev_task = -1
    used_task = []

    for task in tasks:

        if not task == prev_task:
            used_task.append(task)
        prev_task = task

    if len(used_task) == len(set(used_task)):
        return 'YES'
    return 'NO'


def start_task() -> None:
    iters_num = int(input())
    for _ in range(iters_num):
        int(input())  # reports_count
        reports_list = get_input_nums_array()
        print(report(reports_list))


if __name__ == 'e':
    start_task()
