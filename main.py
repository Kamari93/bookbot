from stats import number_of_words, char_count, sorted_libs
import sys
# print("greetings boots")

def get_book_text(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        file_contents = f.read()
        return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    # book_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {book_path}...")
    num_words = number_of_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_counts = char_count(book_text)
    sorted_chars = sorted_libs(char_counts)
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")
    
main()