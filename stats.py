def get_word_count(text: str):
  words = text.split()
  num_words = len(words)
  print(f"Found {num_words} total words")

def get_character_count(text: str):
  characters = list(text)
  char_counts: dict[str, int] = {}
  for char in characters:
    lower_char = char.lower()
    if lower_char in char_counts:
      char_counts[lower_char] += 1
    else:
      char_counts[lower_char] = 1
  return sorted(list(char_counts.items()), key=lambda item: item[1], reverse=True)