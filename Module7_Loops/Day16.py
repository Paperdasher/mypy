##Day 16: For Loops

"""
Last time, we learned what a while loop is. While loops are basic loops that help us repeat actions as long as the boolean statement is True.
Although while loops are an easy implementation of loops, they can be less functional in some cases.
For loops can be an easier method to iterate through data types.
"""


def foo(a):
    for x in a:
        print(x)
    
foo(["a", "b", "c", "d"])



#We can also use the range type to iterate through.
import random

def foo2(num):
    a = range(num)
    nums = []
    for n in a:
        nums.append(random.randint(0, 10))
    return nums

print(foo2(10))


# -------------------------------------------------- #

"""
Exercises:

1. 
2. 
3. 
"""

## CODE BELOW ##


# ------------------------------------------- #

## HW: Do three of the Loops problems in the CodingBat page.
