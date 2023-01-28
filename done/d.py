from pprint import pprint as pp

input_table = [
    [3, 4, 1],
    [2, 2, 5],
    [2, 4, 2],
    [2, 2, 1],
]

input_table1 = [
    [2, 11, 72],
    [99, 11, 13],
    [2, 8, 13],
]

clicks_list = [2, 1, 3]
clicks_list1 = [2, 3, 2, 1, 2]

correct_result = [
    [2, 2, 1],
    [3, 4, 1],
    [2, 4, 2],
    [2, 2, 5],
]
correct_result1 = [
    [2, 8, 13],
    [2, 11, 72],
    [99, 11, 13],
]


def sort_rule(x, sort_index, row_length):
    # поумнее ставить гланвынй индекс в начало массива
    return [x[sort_index - 1]] + [x[i] for i in range(row_length) if not i == sort_index - 1]

def sort_table(table: list, sort_index: int, row_length: int):
    return sorted(table, key=lambda x: sort_rule(x, sort_index, row_length))


def compare_arrays(table_one, table_two):
    equal = True
    for i in range(len(table_one)):
        if not table_one[i] == table_two[i]:
            equal = False
    return equal


def click_tabel(table, clicks):
    clicked_table = table
    for click in clicks:
        clicked_table = sort_table(table, click, len(table[0]))
    return clicked_table


res = click_tabel(input_table1, clicks_list1)

pp(res)
pp(correct_result1)
pp(compare_arrays(res, correct_result1))
