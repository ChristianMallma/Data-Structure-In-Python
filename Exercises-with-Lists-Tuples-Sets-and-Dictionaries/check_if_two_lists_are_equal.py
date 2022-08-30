def check_if_two_lists_are_equal(first_list: list[int], second_list: list[int]):
  if len(first_list) != len(second_list):
    return False
  
  first_list.sort()
  second_list.sort()

  if first_list == second_list:
    return True
  else:
    return False

# Test
print(check_if_two_lists_are_equal([1,2,4,5,6], [6,5,4,2,1]))
print(check_if_two_lists_are_equal([1,1,2,4,5,6], [6,5,4,1,2,1]))
print(check_if_two_lists_are_equal([1,1,2,4,5,6], [6,5,4,1,2,3]))