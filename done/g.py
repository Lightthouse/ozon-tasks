from collections import Counter

input_table = [
    [4, 3],
    [3, 1],
    [1, 2],
    [2, 4],
    [2, 5],
    [6, 8],
]

friends_list = [i for i in range(1, 9)]  # нужно брать из ввода

correct_result = [
    [4],
    [3],
    [2],
    [1],
    [1, 4],
    [0],
    [0],
    [0],
]


# TODO 7 пользователя нет в вводе, но в ввыводе есть!


# 1 -> 2 1 -> 3

def create_fiends_dicts(table: [[int]], users):
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


print(create_fiends_dicts(input_table, friends_list))
# print(input_couples)
