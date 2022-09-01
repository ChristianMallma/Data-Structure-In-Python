# Factorial

def factorial(number):
  if number == 0:
    return 1
  
  return number*factorial(number-1)


# Test
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))