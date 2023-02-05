
def get_pages_from_range(str_range):
    left_range, right_range = str_range.split('-')
    return [page for page in range(int(left_range), int(right_range) + 1)]


def get_unprinted_pages(printed_pages, pages_count):
    printed_pages = set(printed_pages)
    all_pages = [page for page in range(1, pages_count + 1)]
    for printed_page in printed_pages:
        all_pages.remove(printed_page)

    return all_pages


def split_nums_list_by_range(all_pages):
    comma_pages = []
    range_pages = []
    range_start = all_pages[0]
    range_end = all_pages[0]

    for unprinted_page in all_pages[1:]:

        if (range_end + 1) == unprinted_page:
            range_end += 1
            continue
        else:
            if range_start == range_end:
                comma_pages.append(str(range_start))
            else:
                prev_range = f'{range_start}-{range_end}'
                range_pages.append(prev_range)

            range_start = unprinted_page
            range_end = unprinted_page

    if range_start == range_end:
        comma_pages.append(str(range_start))
    else:
        prev_range = f'{range_start}-{range_end}'
        range_pages.append(prev_range)

    return ','.join(range_pages + comma_pages)


def find_unprinted_pages(request_table):
    result = []
    for pages_count, pages_printed_str in request_table:

        printed_pages = []
        for pg in pages_printed_str.split(','):
            if '-' in pg:
                printed_pages += get_pages_from_range(pg)
                continue

            printed_pages.append(int(pg))

        unprinted_pages = get_unprinted_pages(printed_pages, pages_count)
        result.append(split_nums_list_by_range(unprinted_pages))

    return result


def get_input_nums_array():
    return [int(inp) for inp in input().split(' ')]


def start_task():
    print_request_count = int(input())
    request = []
    for _ in range(print_request_count):
        pages_count = int(input())
        printed_pages = input()
        request.append((pages_count, printed_pages))

    result = find_unprinted_pages(request)
    for res in result:
        print(res)


def start_local_matching():
    from functions import get_test_param_files
    TEST_NAME = 'f'

    def _get_mock_request_data(request_file: str):
        with open(request_file, 'r') as mf:
            request_count = int(mf.readline())
            mock_table = []
            for _ in range(request_count):
                pages_count = int(mf.readline())
                pages_printed = mf.readline()[:-1]

                mock_table.append((pages_count, pages_printed))

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

    test_num = 1
    request_file, result_file = get_test_param_files(TEST_NAME, test_num)

    request = _get_mock_request_data(request_file)
    correct_result = _get_mock_result_data(result_file)
    calculate_result = find_unprinted_pages(request)

    return correct_result, calculate_result, correct_result == calculate_result

# rs = start_local_matching()
