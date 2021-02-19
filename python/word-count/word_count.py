import re


def count_words(sentence):
    words_dictionary = {}
    for word in [a.strip("'") for a in re.split(r",|\s", sentence) if a]:
        if word in words_dictionary:
            words_dictionary[word] += 1
        else:
            words_dictionary[word] = 1

    return words_dictionary
