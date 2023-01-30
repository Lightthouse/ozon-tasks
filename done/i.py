# Готовые задачи в попке done
mock_processors = [3, 2, 6, 4]
mock_tasks = [[1, 3], [2, 5], [3, 7], [4, 10], [5, 5], [6, 100], [9, 2], ]
correct_result = 105


# input
# 4 7
# 3 2 6 4
# 1 3
# 2 5
# 3 7
# 4 10
# 5 5
# 6 100
# 9 2

# output
# 105

def calculate_tasks_completing_time(tasks, processors):
    work_time = tasks[:-2:-1][0][0] # время запуска последней задачи

    processes_loading = {proc: 0 for proc in sorted(processors)}
    tasks_dict = {time: duration for time, duration in tasks}
    total_energy = 0
    # можно делать не на каждую секнду, а на кажды процесс

    # Распределяем задачи по процессам каждый тик
    for sec in range(1, work_time + 1):

        for pr_num, pr_load in processes_loading.items():
            pr_lost_time = processes_loading[pr_num]
            if pr_lost_time == 0:
                processes_loading[pr_num] = pr_lost_time
            else:
                total_energy += pr_num
                processes_loading[pr_num] = pr_lost_time - 1

        current_task = tasks_dict.get(sec, None)
        if not current_task:
            continue

        free_process = {proc: lost_time for proc, lost_time in processes_loading.items() if lost_time == 0}

        if not free_process:
            continue

        fast_process = min(free_process)
        processes_loading[fast_process] = current_task

    # Прибавим оствшиеся на процессорах задачи
    total_energy += sum(lost_time * proc for proc, lost_time in processes_loading.items())

    return total_energy


def get_input_nums_array():
    return [int(inp) for inp in input().split()]


tasks_list = []
n_processors, m_tasks = get_input_nums_array()
processors_list = get_input_nums_array()

for task in range(m_tasks):
    time_moment, time_duration = get_input_nums_array()
    tasks_list.append([time_moment, time_duration])

print(calculate_tasks_completing_time(tasks_list, processors_list))


# local test varian
# print(calculate_tasks_completing_time(mock_tasks, mock_processors))
