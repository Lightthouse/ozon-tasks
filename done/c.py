input_arr = [2, 1, 3, 1, 1, 4]
input_arr1 = [1, 4, 2, 5, 4, 2, 6, 3]
input_arr2 = [2, 1, 3, 1, 1, 4]
input_arr3 = [2, 1, 3, 1, 1, 4]


MAX_LEVEL = 100

def tmp(couples_list: [int]):
    res = []
    for proger_index in range(len(couples_list)):

        current_proger = couples_list[proger_index]

        if current_proger > MAX_LEVEL:
            continue

        abs_levels_list = [abs(i - current_proger) for i in couples_list]
        min_level_dif = min(abs_levels_list[proger_index + 1:])
        coproger_index = abs_levels_list.index(min_level_dif, proger_index + 1)

        couples_list[coproger_index] = couples_list[coproger_index] + (MAX_LEVEL * 10)

        res.append([proger_index + 1, coproger_index + 1])



    print(res)

tmp(input_arr1)
#