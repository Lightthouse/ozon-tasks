def make_sports_result_dict(results):
    data = {}
    for racer, result in enumerate(results):
        if result not in data.keys():
            data[result] = []
        data[result].append(racer)
    data = {key: data[key] for key in sorted(data)}
    return data


def get_input_nums_array():
    return [int(inp) for inp in input().split(' ')]


def range_positions(data, result_list):
    position = 1
    next_position = 1
    prev_key = -100
    for current_key, ind in data.items():
        if not (current_key - prev_key) == 1:
            position = next_position
        for i in ind:
            next_position += 1
            result_list[i] = str(position)
        prev_key = current_key

    res = ' '.join(result_list)

    return res


def racing(table):
    result = []
    for sportsman_count, run_results in table:
        result_list = [None] * sportsman_count
        dic = make_sports_result_dict(run_results)
        result.append(range_positions(dic, result_list))

    return result


def start_task():
    request_data_count = int(input())
    request = []
    for _ in range(request_data_count):
        sportsman_count = int(input())
        run_results = get_input_nums_array()
        request.append([sportsman_count, run_results])

    result = racing(request)
    for res in result:
        print(res)


if __name__ == 'd':
    start_task()
