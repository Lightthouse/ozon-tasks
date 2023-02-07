from functions import get_test_param_files, count_tests
from sandbox_tasks import validate_dates

TEST_NAME = 'f'


def _get_mock_request_data(request_file: str):
    with open(request_file, 'r') as mf:
        data_request_count = int(mf.readline())
        request = []
        for _ in range(int(data_request_count)):
            date_ranges_count = int(mf.readline())
            ranges_list = []
            for date_range in range(date_ranges_count):
                ranges_list.append(mf.readline()[:-1])

            request.append(ranges_list)

    return request


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

    request = _get_mock_request_data(request_file)
    correct_result = _get_mock_result_data(result_file)

    calculate_result = []
    for ranges_list in request:
        calculate_result.append(validate_dates(ranges_list))

    return correct_result, calculate_result


def test_f():
    test_files_count = count_tests(TEST_NAME)

    for test_file in range(1, test_files_count + 1):
        correct_result, calculate_result = _test_task_on_file(test_file)
        assert correct_result == calculate_result
