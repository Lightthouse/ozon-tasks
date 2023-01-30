# input_dictionary = ['id']
mock_dictionary = ['task', 'decide', 'id']

mock_request = ['flask', 'code', 'void', 'forces', 'id', 'ask']

correct_results = ['task', 'decide', 'id', 'task', 'decide', 'task']


# input
# 3
# task
# decide
# id
# 6
# flask
# code
# void
# forces
# id
# ask

# output
# task
# decide
# id
# task
# decide
# task

MAX_RHYME_LENGTH = 3
def create_reverse_dict(dictionary: [str]):
    dict_with_reverse_words = [i[::-1] for i in dictionary]
    reverse_dict = {}
    for current_word in dict_with_reverse_words:
        max_word_offset = MAX_RHYME_LENGTH if len(current_word) >= MAX_RHYME_LENGTH else len(current_word)

        for word_offset in range(max_word_offset, 0, -1):
            if reverse_dict.get(current_word[:word_offset], None):
                reverse_dict[current_word[:word_offset]].append(current_word[::-1])
            else:
                reverse_dict[current_word[:word_offset]] = [current_word[::-1]]

    return reverse_dict


def find_word_rhyme(word: str, dictionary: [str], reverse_dictionary):
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

    rhyme = make_rhyme(word, dictionary, reverse_dictionary)

    return rhyme


def find_rhymes(words: [str], dictionary):
    res = []
    reverse_dict = create_reverse_dict(dictionary)
    for word in words:
        res.append(find_word_rhyme(word, dictionary, reverse_dict))
    return res


n_dictionary = int(input())  # 3
dictionary = []
words = []
for wrd in range(n_dictionary):
    dictionary.append(input())

q_words = int(input())
for wrd in range(q_words):
    words.append(input())

for r in find_rhymes(words, dictionary):
    print(r)


# local test variant
# print(*find_rhymes(mock_request, mock_dictionary))

