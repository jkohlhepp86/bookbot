from stats import word_count
from stats import char_count
from stats import order_count
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
    return file_contents

def main():
    grab_text = get_book_text(path_to_book)
    wc_print = word_count(grab_text)
    char_counts = char_count(grab_text)
    sorted_counts = order_count(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {wc_print} total words")
    print("--------- Character Count -------")
    for c in sorted_counts:
        char = c["char"]
        count = c["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()