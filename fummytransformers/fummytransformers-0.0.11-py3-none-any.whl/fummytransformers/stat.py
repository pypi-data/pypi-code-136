from files import read_file
import re


def count_words(file, punctuation=False):
    if punctuation:
        return len(read_file(file).split())
    else:
        return len(re.findall(r'\S+', read_file(file)))

if __name__ == "__main__":

    print(count_words("test.txt" print(read_file("test.txt").split())
    # print(word_counter)
    # test = list(open("test.txt", 'r'))

    # print(read_file("test.txt"))
# else:
    # print("Executed when imported")
