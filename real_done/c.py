import re


def match_string_to_car_number(strings_table):
    result = []

    first_type = r'\D{1}\d{1}\D{2}'
    second_type = r'\D{1}\d{2}\D{2}'

    for row in strings_table:
        first_type_nums = re.findall(first_type, row)
        second_type_nums = re.findall(second_type, row)

        first_type_nums = first_type_nums if first_type_nums else []
        second_type_nums = second_type_nums if second_type_nums else []

        all_types_nums = first_type_nums + second_type_nums
        all_types_nums_sum = sum((len(word) for word in all_types_nums))

        if not len(row) == all_types_nums_sum:
            result.append('-')
            continue

        car_num_indexes = dict()
        indexes_dict = dict()

        for car_num in all_types_nums:

            current_car_num_index = row.index(car_num)

            if not car_num_indexes.get(car_num):
                car_num_indexes[car_num] = [current_car_num_index]

                indexes_dict[current_car_num_index] = car_num
                continue



            car_num_existing_indexes = car_num_indexes[car_num]
            if current_car_num_index not in car_num_existing_indexes:
                car_num_indexes[car_num].append(current_car_num_index)

                indexes_dict[current_car_num_index] = car_num

            else:
                max_index = max(car_num_existing_indexes) + 1
                current_car_num_index = row.index(car_num, max_index)
                car_num_indexes[car_num].append(current_car_num_index)

                indexes_dict[current_car_num_index] = car_num

        sorted_car_nums_list = [indexes_dict[word_index] for word_index in sorted(indexes_dict)]
        no_whitespace_string = ''.join(sorted_car_nums_list)

        if not no_whitespace_string == row:
            result.append('-')
            continue
        res_str = ' '.join(sorted_car_nums_list)
        result.append(res_str)

    return result


def get_input_nums_array():
    return [int(inp) for inp in input().split(' ')]


def start_task():
    string_count = int(input())
    request = []
    for _ in range(string_count):
        request.append(input())

    result = match_string_to_car_number(request)
    for res in result:
        print(res)


def start_local_matching():
    from functions import get_test_param_files
    TEST_NAME = 'c'

    def _get_mock_request_data(request_file: str):
        with open(request_file, 'r') as mf:
            rows_count = int(mf.readline())
            mock_table = []
            for _ in range(rows_count):
                mock_table.append(mf.readline()[:-1])

        return mock_table, rows_count

    def _get_mock_result_data(result_file: str):
        with open(result_file, 'r') as mf:
            mock_result = []
            while True:
                row = mf.readline()

                if '-' in row:
                    mock_result.append('-')
                    continue

                if len(row) <= 1:
                    break
                mock_result.append(row[:-1])
        return mock_result

    test_num = 12
    request_file, result_file = get_test_param_files(TEST_NAME, test_num)

    request, rows_count = _get_mock_request_data(request_file)
    correct_result = _get_mock_result_data(result_file)
    calculate_result = match_string_to_car_number(request)

    return correct_result, calculate_result, correct_result == calculate_result

rs = start_local_matching()
print(rs[0])
print(rs[1])
print(rs[2])
