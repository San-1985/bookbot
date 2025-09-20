
from stats import get_word_count, get_char_count, get_text

def main():
    text = get_text("./books/frankenstein.txt")
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document")
    char_count = get_char_count(text)
    print(char_count)
main()

