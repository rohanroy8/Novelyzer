from stats import word_count, char_count, word_frequency
import sys

def get_book_text(path: str):
    with open(path) as f:

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        contents = f.read()

        count = word_count(contents)
        print("----------- Word Count ----------")
        print(f"Found {count} words in the file")

        word_list: list[tuple[str,int]] = word_frequency(contents)

        print("--------- Top 10 Word Frequency -------")
        for key, value in word_list[:10]:
            print(f"{key} : {value}")

        print("============= END ===============")

if len(sys.argv) < 2:
    print("usage: python main.py <file>")
    sys.exit(1)
path = sys.argv[1]
get_book_text(path)
