from copy import deepcopy
from typing import List

UNREACHABLE_ELEMENT = 999


def sort_indexes(click: int, tables_copy: List[List], n: int, indexes: List):
    for _ in range(n):
        ind = tables_copy[click - 1].index(min(tables_copy[click - 1]))
        indexes.append(ind)
        tables_copy[click - 1][ind] = UNREACHABLE_ELEMENT
    return indexes


def sort_tables(n: int, tables: List[List], indexes: List[List]):
    for i, table in enumerate(tables, start=0):
        new_table = [None] * n
        for y in range(len(table)):
            new_table[y] = table[indexes[y]]
        tables[i] = new_table


def start(output: str):
    for loop in range(int(input())):
        input_table = []
        tables = []
        indexes = []

        _ = input()

        size = input()
        n = int(size.split(' ')[0])
        m = int(size.split(' ')[1])

        for i in range(m):
            tables.append([])

        for _ in range(n):
            input_table.append([int(x) for x in input().split(' ')])

        for i in input_table:
            for y in range(len(i)):
                tables[y].append(i[y])

        _ = input()
        clicks = [int(x) for x in input().split(' ')]

        for click in clicks:
            tables_copy = deepcopy(tables)
            sort_indexes(click, tables_copy, n, indexes)
            sort_tables(n, tables, indexes)
            indexes.clear()

        row_range = range(len(tables[0]))

        for i in row_range:
            cl = [str(t[i]) for t in tables]
            output += ' '.join(cl) + '\n'
        output += '\n'

    return output


result = ''
print(start(result))
