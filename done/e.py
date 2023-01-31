# Itertools проникнуться

mock_tables = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 1],
    [2, 3, 4, 8, 5, 5, 5, 5],
    [1, 1, 3, 2, 2],
    [1, 1, 2, 3, 2],
]

correct_results = ['YES', 'NO', 'YES', 'YES', 'NO']

# input
# 5
# 5
# 1 2 3 4 5
# 4
# 1 2 3 1
# 8
# 2 3 4 8 5 5 5 5
# 5
# 1 1 3 2 2
# 5
# 1 1 2 3 2

# output
# YES
# NO
# YES
# YES
# NO


def get_input_nums_array():
    return [int(inp) for inp in input().split(' ')]

def report(tasks):
    prev_task = -1
    used_task = []

    for task in tasks:

        if not task == prev_task:
            used_task.append(task)
        prev_task = task

    if (len(used_task) == len(set(used_task))):
        return 'YES'
    return 'NO'


iters_num = int(input())
for i in range(iters_num):
    reports_count = int(input())
    reports_list = get_input_nums_array()
    print(report(reports_list))

    # local test variant
    # def whole_report(all_programmers_tasks: [[int]]):
    #     result_report = []
    #     for tasks in all_programmers_tasks:
    #         result_report.append(report(tasks))

#     return result_report
#
# print(whole_report(mock_tables))
# print(correct_results)

