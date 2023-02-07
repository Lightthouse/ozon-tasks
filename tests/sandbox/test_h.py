from functions import get_test_param_files, count_tests
from sandbox_tasks import validate_map

TEST_NAME = 'h'


def _get_mock_request_data(request_file: str):
    with open(request_file, 'r') as mf:

        data_request_count = int(mf.readline())
        mock_table = []
        for _ in range(int(data_request_count)):

            n_rows, m_cols = [int(i) for i in mf.readline().split()]
            current_table = []

            for row in range(n_rows):
                current_table.append(mf.readline()[:-1])

            mock_table.append((current_table, m_cols, n_rows))

    return mock_table


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

    geks_table = _get_mock_request_data(request_file)
    correct_result = _get_mock_result_data(result_file)

    calculate_result = []
    for table in geks_table:
        calculate_result.append(validate_map(table[0], table[1], table[2]))

    return correct_result, calculate_result


def test_h():
    test_files_count = count_tests(TEST_NAME)

    for test_file in range(1, test_files_count + 1):
        correct_result, calculate_result = _test_task_on_file(test_file)
        assert correct_result == calculate_result
