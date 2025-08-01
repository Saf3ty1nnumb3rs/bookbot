import sys
from stats import get_character_count, get_word_count

def get_book_text(path_to_file: str):
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents


def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_text = get_book_text(sys.argv[1])
  print("============ BOOKBOT ============")
  print(f"Analyzing books found at {sys.argv[1]}")
  print("----------- Word Count ----------")
  get_word_count(book_text)
  print("---------- Character Count -------")
  char_counts = get_character_count(book_text)
  for key, value in char_counts:
    if key.isalpha():print(f"{key}: {value}")
  print("============= END ===============")

main()
