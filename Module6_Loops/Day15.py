##Day 15: Intro to Loops(while loops)

"""
When we want to perform an operation until some condition turns false, we don't want to write code over and over again.
If we don't know how many repititions we'd need, it's impossible to write out all that code.
We use loops to cover that need. We keep iterating until the condition is invalid, and we exit the code block.
"""

a = 1
while(a < 10):
    print(a) # what do you think this prints? Up to what number?
    a += 1 

print("Final value of a:", a) # what will this print?


"""
We can also use the random module to create random numbers.
This can be useful to make a list of random numbers to test functions such as sorting algorithms.
"""

import random

b = 5
nums = []
while(b > 1): # can write while loops to decend
    nums.append(random.randint(0, 5)) # adds random int from 0 to 5 into nums list
    b -= 1 

print(nums) # how many values will be in the list?

"""
Exercises:

Write a function where...
1. Removes all odd numbers from a list
2. Takes the sum of all elements in the list until a neg num
3. Finds the largest number in a list

"""

### CODE BELOW ### (get rid of pass when writing each function)

def remove_odd(nums):
    pass

def sumlist(nums):
    pass

def largestnum(nums):
    pass

"""
HW: 
1. Create a while loop that asks for a number, and either adds 1 or subtracts 1 until the number is 100.
2. Create a factorial function.
"""