from collections import Counter


# input
# 6
# 12
# 2 2 2 2 2 2 2 3 3 3 3 3
# 12
# 2 3 2 3 2 2 3 2 3 2 2 3
# 1
# 10000
# 9
# 1 2 3 1 2 3 1 2 3
# 6
# 10000 10000 10000 10000 10000 10000
# 6
# 300 100 200 300 200 300

# output
# 22
# 22
# 10000
# 12
# 40000
# 1100

def products_sum(input_list: [int]):
    list_sum = 0
    counted_list = Counter(input_list)
    for price in counted_list:
        list_sum += int(price) * (counted_list[price] - counted_list[price] // 3)
    return list_sum


def get_input_nums_array():
    return [int(inp) for inp in input().split()]


iters_num = int(input())
for i in range(iters_num):
    input_length = int(input())
    input_numbers = get_input_nums_array()

    print(products_sum(input_numbers))
