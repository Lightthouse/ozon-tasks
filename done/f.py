import datetime
from typing import List, no_type_check


@no_type_check
def convert_to_date(dates: str):
    left_range, right_range = dates.split('-')

    try:
        left_range = datetime.datetime.strptime(left_range, '%H:%M:%S').time()
        right_range = datetime.datetime.strptime(right_range, '%H:%M:%S').time()
    except ValueError:
        return False

    if left_range > right_range:
        return False

    return left_range, right_range


def sort_converted_dated(dates: List[str]) -> List:
    converted_dates = []
    for date_range in dates:

        converted_date = convert_to_date(date_range)
        if not converted_date:
            return []

        converted_dates.append(converted_date)

    return sorted(converted_dates, key=lambda x: x[1])


def check_dates_intersections(dates: List) -> bool:
    prev_date = None
    for left_date, right_date in dates:

        if prev_date and left_date <= prev_date:
            return False

        prev_date = right_date
    return True


def validate_dates(dates: List[str]) -> str:
    converted_sorted_dates = sort_converted_dated(dates)
    if not converted_sorted_dates:
        return 'NO'

    dates_ranges_correct = check_dates_intersections(converted_sorted_dates)
    if not dates_ranges_correct:
        return 'NO'

    return 'YES'


def start_task() -> None:
    iters_num = int(input())
    res = []
    for _ in range(iters_num):
        dates_count = int(input())
        dates_list = []
        for _date_range in range(dates_count):
            dates_list.append(input())
        res.append(validate_dates(dates_list))

    for r in res:
        print(r)


start_task()
# local test variant
# def whole_validation(table: [[str]]):
#     res = []
#     for dates in table:
#         res.append(validate_dates(dates))
#
#     return res
#
#
# print(whole_validation(mock_tables))
# print(correct_result)
