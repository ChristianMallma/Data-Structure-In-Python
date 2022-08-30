def compress_repeat_based_string(string: str):
  if len(string) == 0:
    return ""
  letters = dict()
  prev_letter = string[0]
  count = 0
  for letter in string:
    if letter == prev_letter:
      count += 1
    else:
      letters[prev_letter] = count
      count = 1

    prev_letter = letter

  letters[prev_letter] = count

  final_string = str()
  for k in letters:
    final_string = final_string + f"{k}{letters[k]}"

  return final_string

# Test
print(compress_repeat_based_string('AAABB'))
print(compress_repeat_based_string('AAAABBBCCDaaa'))
print(compress_repeat_based_string(''))
print(compress_repeat_based_string('A'))
