
from stats import get_word_count

def main():
    num_words = get_word_count("./books/frankenstein.txt")
    print(f"{num_words} words found in the document")

main()

