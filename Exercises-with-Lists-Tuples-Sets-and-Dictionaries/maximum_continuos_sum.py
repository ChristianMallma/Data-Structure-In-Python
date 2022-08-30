def maximum_continuos_sum(numbers_list: list):
  sum_list = list()
  accumulate = 0
  for number in numbers_list:
    accumulate += number
    sum_list.append(accumulate)
  
  sum_max = max(sum_list)
  
  return sum_max

print(maximum_continuos_sum([4,8,6,-3,2,-4,1,-1]))