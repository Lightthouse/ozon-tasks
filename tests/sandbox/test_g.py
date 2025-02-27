from sandbox_tasks import match_friends
from functions import get_test_param_files, count_tests

TEST_NAME = 'g'


def _get_mock_request_data(request_file: str):
    with open(request_file, 'r') as mf:
        users_count, couple_count = [int(num) for num in mf.readline().split()]
        mock_table = []
        for _ in range(int(couple_count)):
            mock_table.append([int(user) for user in mf.readline().split()])

    return mock_table, users_count


def _get_mock_result_data(result_file: str):
    with open(result_file, 'r') as mf:
        mock_result = []
        while True:
            row = mf.readline()
            if len(row) <= 1:
                break
            mock_result.append([int(i) for i in row.split()])

    return mock_result


def _test_task_on_file(test_num: int):
    request_file, result_file = get_test_param_files(TEST_NAME, test_num)

    couples_table, users_count = _get_mock_request_data(request_file)
    correct_result = _get_mock_result_data(result_file)
    calculate_result = match_friends(couples_table, users_count)

    return correct_result, calculate_result


def test_g():
    test_files_count = count_tests(TEST_NAME)

    for test_file in range(1, test_files_count + 1):
        correct_result, calculate_result = _test_task_on_file(test_file)
        assert correct_result == calculate_result


