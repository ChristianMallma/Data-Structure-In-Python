def sum_of_pairs_of_numbers(numbers: list, value: int):
  # Example: sum_of_pairs_of_numbers([1,3,2,2],4) -> (1,3), (2,2)
  result = list()
  aux_numbers = list()
  for number in numbers:

    total = number
    prev = total

    if len(aux_numbers) == 0:
      aux_numbers = numbers.copy()
    aux_numbers.pop(0)
    new_numbers = aux_numbers.copy()

    if len(new_numbers) == 1:
      total += new_numbers[0]
      if total == value:
        result.append( (number, new_numbers[0]) )

      result = list(set(result))
      return result

    for new_number in new_numbers:
      total += new_number

      if total == value:
        result.append( (number, new_number) )
      
      total = prev
    
    aux_numbers = new_numbers.copy()

# Test
print(sum_of_pairs_of_numbers(numbers=[1,3,2,2,2], value=4))
