from collections import Counter


def sea_battle(ships_table):
    result = []
    correct_row = Counter([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])

    for row in ships_table:
        if not Counter(row) == correct_row:
            result.append('NO')
        else:
            result.append('YES')

    return result


def get_input_nums_array():
    return [int(inp) for inp in input().split(' ')]


def start_task():
    request = []
    rows_num = int(input())
    for _ in range(rows_num):
        request.append(get_input_nums_array)

    result = sea_battle(request)
    for res in result:
        print(res)


start_task()


def start_local_battle():
    from functions import get_test_param_files
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

    test_num = 1
    request_file, result_file = get_test_param_files(TEST_NAME, test_num)

    request, rows_count = _get_mock_request_data(request_file)
    correct_result = _get_mock_result_data(result_file)
    calculate_result = sea_battle(request)

    # eto pzdc
    return correct_result, calculate_result


print(start_local_battle())
