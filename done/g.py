from collections import Counter

mock_tables = [[4, 3], [3, 1], [1, 2], [2, 4], [2, 5], [6, 8], ]

mock_friends_list = [i for i in range(1, 9)]

correct_results = [[4], [3], [2], [1], [1, 4], [0], [0], [0], ]


# input
# 8 6
# 4 3
# 3 1
# 1 2
# 2 4
# 2 5
# 6 8

# output
# 4
# 3
# 2
# 1
# 1 4
# 0
# 0
# 0

def match_friends(table: [[int]], users):
    friends_dict = dict()
    res = []

    for first, second in table:

        if first in friends_dict:
            friends_dict[first].append(second)
        else:
            friends_dict[first] = [second]

        if second in friends_dict:
            friends_dict[second].append(first)
        else:
            friends_dict[second] = [first]

    for user in users:

        existing_friends = friends_dict.get(user, [])
        possible_friends = []

        for fr in existing_friends:
            possible_friends.extend(friends_dict[fr])
            possible_friends.remove(user)

        if not possible_friends:
            res.append([0])
            continue

        counted_possible_friends = Counter(possible_friends)
        max_intersections = max(counted_possible_friends.values())
        mutual_friends = [us for us, count in counted_possible_friends.items() if count == max_intersections]

        res.append(mutual_friends)

    return res


def get_input_nums_array():
    return [int(inp) for inp in input().split(' ')]


friends_count = 8  # 8
iters_num = 6  # 6 (couples count)
friends_list = []
for i in range(iters_num):  # mock_tables
    first_friend, second_friend = get_input_nums_array()  # i
    friends_list.append([first_friend, second_friend])

mutual_friends = match_friends(friends_list, [i for i in range(1, friends_count + 1)])
for friends_couple in mutual_friends:
    print(*friends_couple)

# print(create_fiends_dicts(mock_tables, friends_list))
