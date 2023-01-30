import datetime

mock_tables = [

    ['02:46:00-03:14:59'],

    ['23:59:59-23:59:59',
     '00:00:00-23:59:58'],

    ['23:59:58-23:59:59',
     '00:00:00-23:59:58'],

    ['23:59:59-23:59:58',
     '00:00:00-23:59:57'],

    ['17:53:39-20:20:02',
     '10:39:17-11:00:52',
     '08:42:47-09:02:14',
     '09:44:26-10:21:41',
     '00:46:17-02:07:19',
     '22:42:50-23:17:46'],

    ['24:00:00-23:59:59'],
]
correct_result = ['YES', 'YES', 'NO', 'NO', 'YES', 'NO']


# input
# 6
# 1
# 02:46:00-03:14:59
# 2
# 23:59:59-23:59:59
# 00:00:00-23:59:58
# 2
# 23:59:58-23:59:59
# 00:00:00-23:59:58
# 2
# 23:59:59-23:59:58
# 00:00:00-23:59:57
# 6
# 17:53:39-20:20:02
# 10:39:17-11:00:52
# 08:42:47-09:02:14
# 09:44:26-10:21:41
# 00:46:17-02:07:19
# 22:42:50-23:17:46
# 1
# 24:00:00-23:59:59

# output
# YES
# YES
# NO
# NO
# YES
# NO


def validate_dates(dates_ranges: [str]):
    def convert_to_date(date_range):
        left_range, right_range = date_range.split('-')

        try:
            left_range = datetime.datetime.strptime(left_range, '%H:%M:%S').time()
            right_range = datetime.datetime.strptime(right_range, '%H:%M:%S').time()
        except ValueError:
            return False

        if left_range > right_range:
            return False
        return left_range, right_range

    def sort_converted_dated(dates):
        converted_dates = []
        for date_range in dates:

            converted_date = convert_to_date(date_range)
            if not converted_date:
                return False

            converted_dates.append(converted_date)

        return sorted(converted_dates, key=lambda x: x[1])

    def check_dates_intersections(dates):
        prev_date = None
        for left_date, right_date in dates:

            if prev_date and left_date <= prev_date:
                return False

            prev_date = right_date
        return True

    converted_sorted_dates = sort_converted_dated(dates_ranges)
    if not converted_sorted_dates:
        return 'NO'

    dates_ranges_correct = check_dates_intersections(converted_sorted_dates)
    if not dates_ranges_correct:
        return 'NO'

    return 'YES'


iters_num = int(input())
res = []
for i in range(iters_num):
    dates_count = int(input())
    dates_list = []
    for date_range in range(dates_count):
        dates_list.append(input())
    res.append(validate_dates(dates_list))

for r in res:
    print(r)



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
