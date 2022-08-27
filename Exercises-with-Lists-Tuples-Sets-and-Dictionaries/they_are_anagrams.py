# Function
def they_are_anagrams(first_word: str, second_word: str):
  first_word = first_word.replace(' ', '').lower()
  second_word = second_word.replace(' ', '').lower()

  if first_word == second_word:
    return False
  
  if len(first_word) != len(second_word):
    return False
  
  word_container = dict()

  for letter in first_word:
    if word_container.get(letter):
      word_container[letter] = word_container[letter] + 1
    else:
      word_container[letter] = 1

  for letter in second_word:
    if word_container.get(letter):
      word_container[letter] = word_container[letter] - 1

  for value in word_container.values():
    if value != 0:
      return False
  
  return True

# Testing
print(they_are_anagrams("paris", "prisa"))