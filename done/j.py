# mock_dictionary = ['mask', 'blonde', 'maiden']
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

# можно сделать три массива с обрезанным словарем и провеять, есть ли кусок слова в этих словарях

MAX_RHYME_LENGTH = 3


def create_rhyme_dictionary(dictionary: [str]):
    rhymes_dictionary = {}
    for current_word in dictionary:

        for offset in range(1, 4):

            rhyme_part = current_word[-offset:]
            if len(rhyme_part) < offset:
                continue

            if rhymes_dictionary.get(rhyme_part):
                rhymes_dictionary[rhyme_part].append(current_word)
                continue
            rhymes_dictionary[rhyme_part] = [current_word]

    return rhymes_dictionary


def make_rhyme(word: str, dictionary: [str], rhyme_dictionary):
    rhyme = dictionary[1] if dictionary[0] == word else dictionary[0]

    for word_offset in range(MAX_RHYME_LENGTH, 0, -1):
        rhyme_key = word[-word_offset:]
        if not rhyme_dictionary.get(rhyme_key):
            continue

        if not rhyme_dictionary[rhyme_key][0] == word:
            return rhyme_dictionary[rhyme_key][0]

        try:
            return rhyme_dictionary[rhyme_key][1]
        except:
            pass



    return rhyme


def find_rhymes(words: [str], dictionary):
    res = []
    rhyme_dictionary = create_rhyme_dictionary(dictionary)
    for word in words:
        res.append(make_rhyme(word, dictionary, rhyme_dictionary))
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
# print(find_rhymes(mock_request, mock_dictionary))
