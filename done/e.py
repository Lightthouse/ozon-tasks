# Itertools проникнуться

input_cascade = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 1],
    [2, 3, 4, 8, 5, 5, 5, 5],
    [1, 1, 3, 2, 2],
    [1, 1, 2, 3, 2],
]

correct_result = ['YES', 'NO', 'YES', 'YES', 'NO']


def report(programmer_tasks: [int]):
    used_nums = []
    prev_task = -1

    for index, task in enumerate(programmer_tasks):

        if task in used_nums and not prev_task == task:
            return 'NO'

        used_nums.append(task)
        prev_task = task

    return 'YES'


def whole_report(all_programmers_tasks: [[int]]):
    result_report = []
    for tasks in all_programmers_tasks:
        result_report.append(report(tasks))

    return result_report


print(whole_report(input_cascade))
