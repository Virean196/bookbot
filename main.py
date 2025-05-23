from stats import get_char_count, dict_into_sorted_list, get_word_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:    
        path_to_book = sys.argv[1]
        sorted_list = dict_into_sorted_list(get_char_count(path_to_book))   
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_book}")
        print("----------- Word Count ----------")
        print(f"Found {get_word_count(path_to_book)} total words")
        print("--------- Character Count -------")
        for x in sorted_list:
            if x["char"].isalpha():
                print(f"{x["char"]}: {x["num"]}")
        print("============= END ===============")

main()