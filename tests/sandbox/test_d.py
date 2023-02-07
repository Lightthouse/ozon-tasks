from typing import List

from sandbox_tasks import click_table
from functions import get_test_param_files, count_tests

TEST_NAME = 'd'


def _get_mock_request_data(request_file: str) -> List:
    with open(request_file, 'r') as mf:
        request_data = []
        tables_count = int(mf.readline())

        for _ in range(tables_count):
            mf.readline()
            current_request_data = tuple()
            n_rows, m_cols = [int(i) for i in mf.readline().split()]
            current_table = []
            for _n_row in range(n_rows):
                current_table.append([int(i) for i in mf.readline().split()])

            clicks_count = int(mf.readline())
            clicks = [int(i) for i in mf.readline().split()]

            current_request_data = current_table, clicks, len(current_table), len(current_table[0])

            request_data.append(current_request_data)
    return request_data


def _get_mock_result_data(result_file: str, request_tables_count: int) -> List:
    with open(result_file, 'r') as mf:
        mock_result = []
        for result_index in range(request_tables_count):
            mock_result.append([])

            while True:
                row = mf.readline()
                if len(row) == 1:
                    break
                mock_result[result_index].append([int(i) for i in row.split()])

    return mock_result


def _test_task_on_file(test_num: int):
    request_file, result_file = get_test_param_files(TEST_NAME, test_num)

    request = _get_mock_request_data(request_file)
    tables_count = len(request)

    correct_result = _get_mock_result_data(result_file, tables_count)

    calculate_result = []
    for table_index in range(tables_count):
        calculate_result.append(click_table(*request[table_index]))

    return correct_result, calculate_result


def test_d():
    test_files_count = count_tests(TEST_NAME)

    for test_file in range(1, test_files_count + 1):
        correct_result, calculate_result = _test_task_on_file(test_file)
        assert correct_result == calculate_result
