##Day 10: Intro to Conditionals

"""
Lesson Description:
Cover if, elif, else and make sure to show ==  vs =
Compare two numbers and if they are equal print that they are equal. 
If the first one is equal to 15 print that it is equal to fifteen elif the second number is equal to 60 print that it is equal to sixty, else print out chicken


---
<b>Review:<b> = was an <b>*assignment operator*</b>, meaning it assigns a value to another.

These assign a <b>varible</b> to a value, or another variable. Assignments can occur for variables set to the same data type.
'''
a = 100
b = a
c = b + 10
d = c - 15
'''

What will the following output?

'''
b == a
b != a
c >= d
a < c
'''

---
To do actions given a condition, we can use an <b>if-statement</b>. An if-statement allows to determine whether or not to do operations inside of the block.

'''
if a == b:
  print(a)
'''


# ----------------------------------------------------- #



Exercise:

1. Make a function that takes in a number and if it is not greater than 10, add 2 to the number. If the number is still not greater than 10, return false. Otherwise true.
2. If a string contains "a" return "I like that." If not, return "Aw man." -> Hint: _ in _ checks if a string is in another string


# ------------------------------------------------------ #

"""
HW: 
1. Create a function that takes in a favorite food as a parameter.
- if the food is equal to cake, print out "I like cake too"
- if the food is equal to salad, print out "I don't like salad"
- if the food is neither, print out "Sounds good"

2. Complete make_bricks, lone_sum, lucky_sum, no_teen_sum problems on CodingBat under If-statements.
"""
