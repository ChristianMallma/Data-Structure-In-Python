# Balance punctuation marks
import sys
sys.path.append('/Users/chris/christian/developer/Data-Structures-In-Python')
from stack import Stack

def balanceds(marks_list: str)->bool:
  if len(marks_list) % 2 != 0:
    return False

  parentheses_stack = Stack() # ()
  square_brackets = Stack() # []
  curly_brackets = Stack()  # {}
  
  for mark in marks_list:
    # adding
    if mark == '(':
      parentheses_stack.insert(mark)
    if mark == '[':
      square_brackets.insert(mark)
    if mark == '{':
      curly_brackets.insert(mark)
    
    # deleting
    if mark == ')':
      parentheses_stack.delete()
    if mark == ']':
      square_brackets.delete()
    if mark == '}':
      curly_brackets.delete()
  
  if parentheses_stack.is_empty() and square_brackets.is_empty() and curly_brackets.is_empty():
    return True
  
  return False

# Test
print(balanceds('[]'))
print(balanceds('[](){}'))
print(balanceds('[()]'))
print(balanceds('[]('))
