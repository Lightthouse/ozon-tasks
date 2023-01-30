# количество входных данных
input_data_count = int(input())

def get_input_nums_array():
    return [int(inp) for inp in input().split()]

for iter_num in range(input_data_count):
    first_num, second_num = get_input_nums_array()
    print(first_num + second_num)
