input_arr = [
    [2, 1, 3, 1, 1, 4],
    [5, 5],
    [1, 4, 2, 5, 4, 2, 6, 3],

]

# input
# 3
# 6
# 2 1 3 1 1 4
# 2
# 5 5
# 8
# 1 4 2 5 4 2 6 3

# output
# 1 2
# 3 6
# 4 5
#
# 1 2
#
# 1 3
# 2 5
# 4 7
# 6 8


def find_coproger(couples_list: [int], couples_count: [int]):
    res = []
    for proger_index in range(couples_count):

        current_proger = couples_list[proger_index]

        if current_proger > MAX_LEVEL:
            continue

        abs_levels_list = [abs(i - current_proger) for i in couples_list]
        min_level_dif = min(abs_levels_list[proger_index + 1:])
        coproger_index = abs_levels_list.index(min_level_dif, proger_index + 1)

        couples_list[coproger_index] = couples_list[coproger_index] + (MAX_LEVEL * 10)

        res.append([proger_index + 1, coproger_index + 1])
    return res


def get_input_nums_array():
    return [int(inp) for inp in input().split()]


iters_num = int(input()) # 1
MAX_LEVEL = 100
for i in range(iters_num):
    progers_count = int(input()) # 6
    progers_levels = get_input_nums_array() #  [2, 1, 3, 1, 1, 4]
    for couple in find_coproger(progers_levels, progers_count):
        print(couple[0], couple[1])



