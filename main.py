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
        for i in range(0,11):
            print(f"{word_list[i][0]} : {word_list[i][1]}")

        print("============= END ===============")

path = sys.argv[1]
get_book_text(path)
