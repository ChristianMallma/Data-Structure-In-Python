# Revert string using factorial

def revert_string(string):
  if len(string) <= 1:
    return string
  
  return revert_string(string[1:]) + string[0]

# Test
print(revert_string('abc'))
print(revert_string('mnop'))