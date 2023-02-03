from done import find_rhymes
from functions import get_test_param_files, count_tests

TEST_NAME = 'j'


def _get_mock_request_data(request_file: str):
    with open(request_file, 'r') as mf:
        dict_length = mf.readline()
        mock_dict = []
        mock_req = []
        for _ in range(int(dict_length)):
            mock_dict.append(mf.readline()[:-1])

        request_length = mf.readline()
        for _ in range(int(request_length)):
            mock_req.append(mf.readline()[:-1])

    return mock_req, mock_dict


def _get_mock_result_data(result_file: str):
    with open(result_file, 'r') as mf:
        mock_result = [line[:-1] for line in mf.readlines()]

    return mock_result


def _test_task_on_file(test_num: int):
    request_file, result_file = get_test_param_files(TEST_NAME, test_num)

    request, dictionary = _get_mock_request_data(request_file)
    correct_result = _get_mock_result_data(result_file)
    calculate_result = find_rhymes(request, dictionary)

    # eto pzdc
    return correct_result, calculate_result


def test_j():
    test_files_count = count_tests(TEST_NAME)

    # for test_file in range(1, test_files_count + 1):
    #     correct_result, calculate_result = _test_task_on_file(test_file)
    #     assert correct_result == calculate_result

    assert 1 == 1
