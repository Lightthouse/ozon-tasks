from typing import List, Dict

# mock_dictionary = ['mask', 'blonde', 'maiden']
# mock_dictionary = ['task', 'decide', 'id']
mock_dictionary = ['a', 'kronask', 'anyask']

mock_request = ['flask', 'code', 'void', 'forces', 'id', 'ask']

correct_results = ['task', 'decide', 'id', 'task', 'decide', 'task']

# можно сделать три массива с обрезанным словарем и провеять, есть ли кусок слова в этих словарях

MAX_RHYME_LENGTH = 3


def create_rhyme_dictionary(dictionary: List[str]) -> Dict:
    rhymes_dictionary: Dict[str, list] = {}
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


def make_rhyme(word: str, dictionary: List[str], rhyme_dictionary: Dict) -> str:
    rhyme = dictionary[1] if dictionary[0] == word else dictionary[0]

    for word_offset in range(MAX_RHYME_LENGTH, 0, -1):
        rhyme_key = word[-word_offset:]
        if not rhyme_dictionary.get(rhyme_key):
            continue

        if not rhyme_dictionary[rhyme_key][0] == word:
            return rhyme_dictionary[rhyme_key][0]

        try:
            return rhyme_dictionary[rhyme_key][1]
        except IndexError:
            pass

    return rhyme


def find_rhymes(words: List[str], dictionary: List) -> List:
    res = []
    rhyme_dictionary = create_rhyme_dictionary(dictionary)
    for word in words:
        res.append(make_rhyme(word, dictionary, rhyme_dictionary))
    return res


def start_task() -> None:
    n_dictionary = int(input())  # 3
    dictionary = []
    words = []
    for _ in range(n_dictionary):
        dictionary.append(input())

    q_words = int(input())
    for _ in range(q_words):
        words.append(input())

    for r in find_rhymes(words, dictionary):
        print(r)


start_task()
# local test variant
# print(find_rhymes(mock_request, mock_dictionary))
