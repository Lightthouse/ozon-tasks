import os
import pathlib
from typing import Tuple

TEST_PARAMS_MAIN_FOLDER = 'main_event_test_files'
TEST_PARAMS_SANDBOX_FOLDER = 'sandbox_test_files'


def get_folder_level(pytest_launch: bool = False) -> str:
    # Функция вызывается в разных местах и нужно всегда попадать на тестовые файлы
    current_path = str(pathlib.Path().resolve())
    params_folder = TEST_PARAMS_MAIN_FOLDER if 'main_event' in current_path else TEST_PARAMS_SANDBOX_FOLDER

    if pytest_launch:
        return f'./{params_folder}'

    if params_folder in current_path:
        return f'./{params_folder}'

    return f'../../{params_folder}'


def get_test_param_files(task_name: str, test_num: int, pytest_launch: bool = True) -> Tuple:
    folder = get_folder_level(pytest_launch)

    file_name = str(test_num) if len(str(test_num)) > 1 else '0' + str(test_num)
    mock_params_file = f'{folder}/{task_name}/{file_name}'
    result_file = f'{folder}/{task_name}/{file_name}.a'
    return mock_params_file, result_file


def count_tests(task_name: str, pytest_launch: bool = True) -> int:
    folder = get_folder_level(pytest_launch)

    dir_path = f'{folder}/{task_name}'
    return len(os.listdir(dir_path)) // 2
