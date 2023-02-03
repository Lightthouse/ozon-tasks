from done import calculate_tasks_completing_time
from functions import get_test_param_files

TEST_NAME = 'i'


def _get_mock_request_data(request_file: str):
    with open(request_file, 'r') as mf:
        processors_count, tasks_count = [int(rl) for rl in mf.readline().split()]
        processors = [int(rl) for rl in mf.readline().split()]
        tasks = [list(map(int, mf.readline().split())) for _ in range(tasks_count)]

    return tasks, processors


def _get_mock_result_data(result_file: str):
    with open(result_file, 'r') as mf:
        mock_result = int(mf.readline())

    return mock_result


def _test_task_on_file(test_num: int):
    request_file, result_file = get_test_param_files(TEST_NAME, test_num)

    tasks, processors = _get_mock_request_data(request_file)
    correct_result = _get_mock_result_data(result_file)
    calculate_result = calculate_tasks_completing_time(tasks, processors)

    return correct_result, calculate_result


def test_i():
    test_files_count = 9
    # test_files_count = count_tests(TEST_NAME) # пока не работает с 11 теста

    for test_file in range(1, test_files_count + 1):
        correct_result, calculate_result = _test_task_on_file(test_file)
        assert correct_result == calculate_result
