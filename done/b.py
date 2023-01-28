from collections import Counter


def products_sum(input_list: [int]):
    list_sum = 0
    counted_list = Counter(input_list)
    for price in counted_list:
        list_sum += int(price) * (counted_list[price] - counted_list[price] // 3)
    return list_sum


iters_num = int(input())
total_sum = list()
for i in range(iters_num):
    input_length = int(input())
    input_numbers = [int(i) for i in input().split()]

    total_sum.append(products_sum(input_numbers))
for current_sum in total_sum:
    print(current_sum)
