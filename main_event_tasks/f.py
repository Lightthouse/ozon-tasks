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


if __name__ == 'f':
    start_task()
