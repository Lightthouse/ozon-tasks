# input_dictionary = ['id']
input_dictionary = ['task', 'decide', 'id']

input_request = ['flask', 'code', 'void', 'forces', 'id', 'ask']

correct_result = ['task', 'decide', 'id', 'task', 'decide', 'task']

MAX_RHYME_LENGTH = 3


def find_rhyme(word: str, dictionary: [str]):
    def create_reverse_dict(dict_list: [str]):
        dict_with_reverse_words = [i[::-1] for i in dict_list]
        reverse_dict = {}
        for current_word in dict_with_reverse_words:
            max_word_offset = MAX_RHYME_LENGTH if len(current_word) >= MAX_RHYME_LENGTH else len(current_word)

            for word_offset in range(max_word_offset, 0, -1):
                if reverse_dict.get(current_word[:word_offset], None):
                    reverse_dict[current_word[:word_offset]].append(current_word[::-1])
                else:
                    reverse_dict[current_word[:word_offset]] = [current_word[::-1]]

        return reverse_dict

    def make_rhyme(word_for_rhyme, dict_list, reverse_dict):
        rhyme = dict_list[0]
        reverse_word = word_for_rhyme[::-1]

        for word_offset in range(MAX_RHYME_LENGTH, 0, -1):
            rhymes_list = reverse_dict.get(reverse_word[:word_offset], None)
            if rhymes_list:
                rhyme = rhymes_list[0]

            if rhyme == word_for_rhyme:
                try:
                    rhyme = rhymes_list[1]
                    break
                except IndexError:
                    pass

        rhyme = rhyme if not word == rhyme else dictionary[1]
        return rhyme

    reverse_dict = create_reverse_dict(dictionary)
    rhyme = make_rhyme(word, dictionary, reverse_dict)

    return rhyme


# print(find_rhyme(input_request[1], input_dictionary))

def whole_search(words: [str], dictionary: [str]):
    res = []
    for word in words:
        res.append(find_rhyme(word, dictionary))

    return res


print(whole_search(input_request, input_dictionary))
