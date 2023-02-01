from collections import Counter
from typing import List, Dict

mock_tables = [[4, 3], [3, 1], [1, 2], [2, 4], [2, 5], [6, 8], ]
mock_friends_list = 9
correct_results = [[4], [3], [2], [1], [1, 4], [0], [0], [0], ]


def match_friends(table: List[List[int]], users_count: int) -> List:
    friends_dict: Dict[int, List] = {user: [] for user in range(1, users_count + 1)}
    res = []

    for first, second in table:
        friends_dict[first].append(second)
        friends_dict[second].append(first)

    for user in range(1, users_count + 1):

        existing_friends = friends_dict.get(user, [])
        possible_friends = []

        for fr in existing_friends:
            possible_friends.extend(friends_dict[fr])
            possible_friends = [psf for psf in possible_friends if psf not in existing_friends + [user]]

        if not possible_friends:
            res.append([0])
            continue

        counted_possible_friends = Counter(possible_friends)
        max_intersections = max(counted_possible_friends.values())
        mutual_friends = [us for us, count in counted_possible_friends.items() if count == max_intersections]

        res.append(sorted(mutual_friends))

    return res


def get_input_nums_array() -> List[int]:
    return [int(inp) for inp in input().split(' ')]


def start_task() -> None:
    friends_count, iters_num = get_input_nums_array()
    friends_list = []
    for _ in range(iters_num):
        first_friend, second_friend = get_input_nums_array()
        friends_list.append([first_friend, second_friend])

    mutual_friends = match_friends(friends_list, friends_count)
    for friends_couple in mutual_friends:
        print(*friends_couple)


start_task()

# print(match_friends(mock_tables, mock_friends_list))
