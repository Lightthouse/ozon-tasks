from typing import List, Dict, Tuple

# Готовые задачи в попке done
# mock_processors = [3, 2, 6, 4]
# mock_tasks = [[1, 3], [2, 5], [3, 7], [4, 10], [5, 5], [6, 100], [9, 2], ]
# correct_result = 105


# mock_processors_count, mock_task_count = [1, 1]
mock_processors = [1000000]
mock_tasks = [[1000000000, 1000000]]
correct_result = 1000000000000


def calculate_tasks_completing_time(tasks: List, processors: List[int]) -> int:
    processes_loading: Dict[int, int] = {proc: 0 for proc in sorted(processors)}
    total_energy = 0
    prev_task: Tuple[int, int] = (0, 0)

    for time_appearance, time_duration in tasks:

        task_is_distributed = False

        for pr_num, pr_load in processes_loading.items():

            if pr_load:
                process_time_left = pr_load - (time_appearance - prev_task[0])
                processes_loading[pr_num] = process_time_left if process_time_left > 0 else 0

            if not processes_loading[pr_num] and not task_is_distributed:
                processes_loading[pr_num] = time_duration
                total_energy += time_duration * pr_num
                task_is_distributed = True

        prev_task = (time_appearance, time_duration)

    return total_energy


def get_input_nums_array() -> List[int]:
    return [int(inp) for inp in input().split()]


def start_task() -> None:
    tasks_list = []
    n_processors, m_tasks = get_input_nums_array()
    processors_list = get_input_nums_array()

    for _ in range(m_tasks):
        time_moment, time_duration = get_input_nums_array()
        tasks_list.append([time_moment, time_duration])

    print(calculate_tasks_completing_time(tasks_list, processors_list))


start_task()

# local test varian
# print(calculate_tasks_completing_time(mock_tasks, mock_processors))
