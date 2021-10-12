import string

unique_letters = set(string.ascii_lowercase)


def is_pangram(sentence):
    return len(set(sentence.lower()) & unique_letters) == len(unique_letters)