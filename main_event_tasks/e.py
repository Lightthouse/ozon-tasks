# недоделано
import copy
from collections import Counter
from typing import List


def filter_word(word: str):
    i = 0
    for char in word:
        if i + 1 < len(word) and word[i + 1] == char:

            word = word[:i] + word[(i + 1):]
        else:
            i += 1
    return word


def compare_signs(input_data: List[str]):
    accepted_list = []
    accepted_list_filtered = []
    input_data = ['aabbaabb', 'aaaabbaabb', 'aabbaabb', 'aabbaabbbbb', 'aabbaabb', 'aabbabb', 'aabbaabbbb', 'aabbaabba',
                  'aababaabb', 'abbaabb', 'aaaabbaabb', 'aabbbb']
    for sign in input_data:
        if not accepted_list:
            accepted_list.append(sign)
            accepted_list_filtered.append(filter_word(sign))
        else:
            if sign in accepted_list:
                continue
            else:
                add = False
                filtered_sign = filter_word(sign)

                if filtered_sign in accepted_list_filtered:
                    cnt_acc = Counter()
                    cnt_inp = Counter()

                    copy_list_filtered = copy.deepcopy(accepted_list_filtered)
                    copy_list_accepted = copy.deepcopy(accepted_list)

                    while filtered_sign in copy_list_filtered:
                        for char in copy_list_accepted[copy_list_filtered.index(filtered_sign)]:
                            cnt_acc[char] += 1
                        for char in sign:
                            cnt_inp[char] += 1
                        for key in cnt_acc:
                            if cnt_inp[key] != cnt_acc[key]:
                                if cnt_inp[key] == 1 or cnt_acc[key] == 1:
                                    add = True
                                # if cnt_inp[key]%2 == 1 or cnt_acc[key]%2 == 1:
                                #     add = True

                        ind = copy_list_filtered.index(filtered_sign)
                        copy_list_accepted.pop(ind)
                        copy_list_filtered.pop(ind)

                    if add:
                        accepted_list.append(sign)
                        accepted_list_filtered.append(filtered_sign)

                else:
                    accepted_list.append(sign)
                    accepted_list_filtered.append(filtered_sign)
    print(accepted_list)
    return str(len(accepted_list))


def start(result: str):
    for _ in range(int(input())):
        input_data = []
        for _ in range(int(input())):
            input_data.append(input())
        result += compare_signs(input_data) + '\n'
    return result


output = ''
print(start(output))