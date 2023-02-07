from typing import List
from sandbox_tasks import sum_nums

TEST_NAME = 'a'

nums_for_sum = [(11, 22), (33, 44), (55, 66), (88, -88), (0, 11), (-1, 0)]

def _get_mock_request_data() -> List:
    request_data = nums_for_sum
    return request_data


def _get_mock_result_data() -> List:
    mock_result = [sum(num) for num in nums_for_sum]
    return mock_result


def test_a():
    request = _get_mock_request_data()
    correct_result = _get_mock_result_data()

    calculate_result = []
    for num_couple in request:
        calculate_result.append(sum_nums(num_couple[0], num_couple[1]))

    assert correct_result == calculate_result
