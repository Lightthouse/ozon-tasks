from pprint import pprint as pp

mock_tables = [
    [[3, 4, 1], [2, 2, 5], [2, 4, 2], [2, 2, 1], ],
    [[100], [9], [10]],
    [[2, 11, 72], [99, 11, 13], [2, 8, 13], ]
]

mock_clicks = [[2, 1, 3], [1, 1], [2, 3, 2, 1, 2]]

correct_results = [
    [[2, 2, 1], [3, 4, 1], [2, 4, 2], [2, 2, 5], ],
    [[9], [10], [100]],
    [[2, 8, 13], [2, 11, 72], [99, 11, 13], ]
]


# input
# 3
#
# 4 3
# 3 4 1
# 2 2 5
# 2 4 2
# 2 2 1
# 3
# 2 1 3
#
# 3 1
# 100
# 9
# 10
# 2
# 1 1
#
# 3 3
# 2 11 72
# 99 11 13
# 2 8 13
# 5
# 2 3 2 1 2

# output
# 2 2 1
# 3 4 1
# 2 4 2
# 2 2 5
#
# 9
# 10
# 100
#
# 2 8 13
# 2 11 72
# 99 11 13


def get_input_nums_array():
    return [int(inp) for inp in input().split(' ')]


def sort_rule(x, sort_index, row_length):
    # поумнее ставить гланвынй индекс в начало массива
    return [x[sort_index - 1]] + [x[indx] for indx in range(row_length) if not indx == sort_index - 1]


def sort_table(table: list, sort_index: int, row_length: int):
    return sorted(table, key=lambda x: sort_rule(x, sort_index, row_length))


def click_table(table, clicks, columns):
    clicked_table = table
    for click in clicks:
        clicked_table = sort_table(table, click, columns)
    return clicked_table


# site test varian
iters_num = int(input()) # 1

res = []
for i in range(iters_num):

    _ = input()
    n_rows, m_cols = get_input_nums_array() #  [4, 3]
    current_table = [] # mock_tables[0]
    for n_row in range(n_rows):
        current_table.append(get_input_nums_array())

    clicks_count = int(input()) # 3
    current_clicks = get_input_nums_array() # mock_clicks[0]
    clicked_table = click_table(current_table, current_clicks, m_cols)

    res.append(clicked_table)

for r in res:
    for res_row in r:
        print(*res_row)
    print()



# local test variant
# def compare_arrays(table_one, table_two):
#     equal = True
#     for i in range(len(table_one)):
#         if not table_one[i] == table_two[i]:
#             equal = False
#             break
#
#     return equal
#
#
# for tbl_num in range(len(mock_tables)):
#     mock_table = mock_tables[tbl_num]
#
#     clicked_table = click_table(mock_table, mock_clicks[tbl_num], len(mock_table[0]))
#     correct_table = correct_results[tbl_num]
#     tables_equal = compare_arrays(clicked_table, correct_table)
#     print('equal: ', tables_equal, ' <> ', clicked_table, ' <> ', correct_table)
#
