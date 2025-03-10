## Day 15 HW:

## 1. Create a while loop that asks for a number, and either adds 1 or subtracts 1 until the number is 100.

while n != 100:
  if n < 100:
    n += 1
  else:
    n -= 1


## 2. Create a factorial function.

def factorial(n):
  result = 1
  i = 1
  while i <= n:
    result *= i
    i += 1
  return result
