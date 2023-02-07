import copy
from typing import List, no_type_check

MAX_NUMBER_VALUE = 100


def get_input_nums_array() -> List[int]:
    return [int(inp) for inp in input().split(' ')]


def click_table(input_table: List, clicks: List, rows_count: int, columns_count: int) -> List:
    tables: List[List[int]] = [[] for colm in range(columns_count)]
    result = []
    indexes: List[int] = []

    def sort_indexes(click: int) -> None:
        for _ in tables_copy[click - 1]:
            ind = tables_copy[click - 1].index(min(tables_copy[click - 1]))
            indexes.append(ind)
            tables_copy[click - 1][ind] = MAX_NUMBER_VALUE * 2

    @no_type_check
    def sort_tables(n: int) -> None:
        for column, table in enumerate(tables, start=0):
            new_row = [None] * n
            for row_table in range(len(table)):
                new_row[row_table] = table[indexes[row_table]]  # type: ignore
            tables[column] = new_row  # type: ignore

    for row in input_table:
        for col_value in range(columns_count):
            tables[col_value].append(row[col_value])

    for click in clicks:
        tables_copy = copy.deepcopy(tables)
        sort_indexes(click)
        sort_tables(rows_count)
        indexes.clear()

    row_range = range(len(tables[0]))
    for row in row_range:
        cl = [t[row] for t in tables]
        result.append(cl)

    return result


def start_task() -> None:
    iters_num = int(input())  # 1

    res = []
    for _i in range(iters_num):

        _ = input()
        n_rows, m_cols = get_input_nums_array()
        current_table = []
        for _n_row in range(n_rows):
            current_table.append(get_input_nums_array())

        int(input())  # clicks_count
        current_clicks = get_input_nums_array()
        clicked_table = click_table(current_table, current_clicks, n_rows, m_cols)

        res.append(clicked_table)

    for r in res:
        for res_row in r:
            print(*res_row)
        print()


if __name__ == 'd':
    start_task()
