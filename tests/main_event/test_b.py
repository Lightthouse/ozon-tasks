from functions import get_test_param_files, count_tests
from main_event_tasks import sea_battle

TEST_NAME = 'b'


def _get_mock_request_data(request_file: str):
    with open(request_file, 'r') as mf:
        rows_count = int(mf.readline())
        mock_table = []
        for _ in range(rows_count):
            mock_table.append([int(num) for num in mf.readline().split()])

    return mock_table, rows_count


def _get_mock_result_data(result_file: str):
    with open(result_file, 'r') as mf:
        mock_result = []
        while True:
            row = mf.readline()
            if len(row) <= 1:
                break
            mock_result.append(row[:-1])
    return mock_result



def _test_task_on_file(test_num: int):
    request_file, result_file = get_test_param_files(TEST_NAME, test_num)
    request, rows_count = _get_mock_request_data(request_file)
    correct_result = _get_mock_result_data(result_file)
    calculate_result = sea_battle(request)

    return correct_result, calculate_result

def test_b():
    test_files_count = count_tests(TEST_NAME)

    for test_file in range(1, test_files_count + 1):
        correct_result, calculate_result = _test_task_on_file(test_file)
        assert correct_result == calculate_result

