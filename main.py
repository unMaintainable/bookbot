from stats import sort_chars_dict, get_num_words
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print(f"""
============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {get_num_words(file_path)} total words
--------- Character Count -------
{"\n".join(map(lambda x: f"{x['char']}: {x['num']}", sort_chars_dict(file_path)))} 
============= END ===============
    """)


main()