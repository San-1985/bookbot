
from stats import get_word_count, get_char_count, get_text, sort_dict
import sys

def print_report(sorted_list, book, num_words):
    report_start = f"\n============ BOOKBOT ============\nAnalyzing book found at {book}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------"

    report_end = "============= END ==============="
    print(report_start)
    for entry in sorted_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print(report_end)

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_text(book)
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document")
    char_count = get_char_count(text)
    sorted = sort_dict(char_count)
    print_report(sorted, book, num_words)

main()

