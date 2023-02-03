from typing import List, Dict, Tuple


def calculate_tasks_completing_time(tasks: List, processors: List) -> int:
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


def calculate_tasks_completing_time_in_progress2(tasks: List, processors: List[int], processors_count: int) -> List:
    # Как то нужно быстрее всё написать
    processors = sorted(processors)
    print(processors[:10:])
    prev_task_dur = 0
    first_proc_on = []
    for time_appearance, time_duration in tasks:
        if time_appearance >= prev_task_dur:
            prev_task_dur = time_appearance + time_duration
            first_proc_on.append((time_appearance, time_duration))

    print(len(first_proc_on))
    return first_proc_on


def calculate_tasks_completing_time_in_progress(tasks: List, processors: List[int], processors_count: int) -> int:
    total_energy = 0

    def find_stopped_proc(proc_status: List, stop_time: int) -> int:
        stopped_proc = -1

        # разворачивать массив
        for proc_index, proc_stop_time in enumerate(proc_status):

            if stop_time >= proc_stop_time:
                return proc_index

        return stopped_proc

    processes_loading = [0] * processors_count
    process_speed = sorted(processors)

    used_processors: List[int] = []
    used_processors_duration: List[int] = []

    for time_appearance, time_duration in tasks:

        # Освобождаем только один процессор, завершивший работу (якобы выбираем самый быстрый из них)
        stopped_proc = find_stopped_proc(used_processors_duration, time_appearance)
        if stopped_proc > -1:
            used_proc = used_processors[stopped_proc]
            processes_loading[used_proc] = 0
            del used_processors[stopped_proc]
            del used_processors_duration[stopped_proc]

        try:
            # Ищем самый быстрый (левый) процессор из свободных
            fastest_processor = processes_loading.index(0)
            processes_loading[fastest_processor] = time_appearance + time_duration
            total_energy += process_speed[fastest_processor] * time_duration

            used_processors.append(fastest_processor)
            used_processors_duration.append(time_appearance + time_duration)
        except ValueError:
            # все процессоры заняты
            continue

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

# start_task()
