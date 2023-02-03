import os
from typing import Tuple

TEST_PARAMS_FOLDER = 'tests_params'


def get_folder_level() -> str:
    current_dir = os.listdir()

    if TEST_PARAMS_FOLDER in current_dir:
        return f'./{TEST_PARAMS_FOLDER}'

    return f'../{TEST_PARAMS_FOLDER}'


def get_test_param_files(task_name: str, test_num: int) -> Tuple:
    folder = get_folder_level()

    file_name = str(test_num) if len(str(test_num)) > 1 else '0' + str(test_num)
    mock_params_file = f'{folder}/{task_name}/{file_name}'
    result_file = f'{folder}/{task_name}/{file_name}.a'
    return mock_params_file, result_file


def count_tests(task_name: str) -> int:
    folder = get_folder_level()

    dir_path = f'{folder}/{task_name}'
    return len(os.listdir(dir_path)) // 2
