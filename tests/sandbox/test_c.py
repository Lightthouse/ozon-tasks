from functions import get_test_param_files, count_tests
from sandbox_tasks import find_coproger

TEST_NAME = 'c'


def _get_mock_request_data(request_file: str):
    with open(request_file, 'r') as mf:
        data_request_count = int(mf.readline())
        request = []
        for _ in range(int(data_request_count)):
            nums_count = int(mf.readline())
            nums_list = [int(i) for i in mf.readline().split()]

            request.append((nums_list, nums_count))

    return request


def _get_mock_result_data(result_file: str, data_count: int):
    with open(result_file, 'r') as mf:
        mock_result = []
        for i in range(data_count):
            while True:
                row = mf.readline()
                if len(row) <= 1:
                    break
                mock_result.append([int(num) for num in row.split()])
    return mock_result


def _test_task_on_file(test_num: int):
    request_file, result_file = get_test_param_files(TEST_NAME, test_num)

    request = _get_mock_request_data(request_file)
    correct_result = _get_mock_result_data(result_file, len(request))

    calculate_result = []
    for progers_list, progers_count in request:
        calculate_result += find_coproger(progers_list, progers_count)

    return correct_result, calculate_result


def test_c():
    test_files_count = count_tests(TEST_NAME)

    for test_file in range(1, test_files_count + 1):
        correct_result, calculate_result = _test_task_on_file(test_file)
        assert correct_result == calculate_result
