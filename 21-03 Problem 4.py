import string

def ispangram(sentence):

    alphabet_set = set(string.ascii_lowercase)

    sentence_set = set(sentence.lower())

    return alphabet_set <= sentence_set

sentence1 = "The quick brown fox jumps over the lazy dog"
sentence2 = "Crazy Fredrick bought many very exquisite opal jewels"


if ispangram(sentence1):
    print(f"\"{sentence1}\" is a pangram.")
else:
    print(f"\"{sentence1}\" is not a pangram.")


if ispangram(sentence2):
    print(f"\"{sentence2}\" is a pangram.")
else:
    print(f"\"{sentence2}\" is not a pangram.")
