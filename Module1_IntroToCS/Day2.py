##Day 2: Type Casting, Advanced Data Types


## bool
"""
A boolean is a concept of True and False. If somebody asks you "Can humans time-travel?" your answer most likely will be "No."
We can assess that this question was a True or False question, so your answer in boolean terms would be false.
Most terms in Python will return True if you put it in boolean terms. But, some values are considered false.
False, None, 0, "", (), [], {} will all return false. Basically, empty elements, the boolean False, None, and 0 will give you False.
This means that, when we deal with numbers, we can use 0 and 1 as binary terms to return True and False values.
"""

#### Try creating a string variable, and printing it


## range
"""
A range is what it sounds like, a sequence of numbers. We can be creative about what kind of sequence we want.
A range is a sequence type, so it isn't considered numeric. This means that range is just like a list or tuple, just in a different format.
By default, the sequence starts at 0 and increments by 1.

range(start, stop, increment)

The only required element here is the stop. When only one number is given in the (), it is assumed default val for the other two vals.
If there are two nums (a, b), it is assumed the start and stop value. 
This means that if you want an increment, you must have all three values, even if you'd like to start at the default 0.
"""

#### Try creating a range variable, and printing it
# What does printing range look like? How would you print each individual value in the sequence?(more in future lessons)


#------------------------------------------------------------------------------------------------------------------------------#


#We can assign multiple variables in one line, making our code more easily readable
a, b, c = "Barack", "Donald", "Joe"
print(a), print(b), print(c)

#We can also assign multiple variables to the same value
d = e = f = "Canada"
print(d), print(e), print(f)

#We can unpack a data structure using variables.
Days = ["Monday", "Tuesday", "Wednesday"]
g, h, i = Days
print(Days)
print(g, h, i)

##Just like string concatenation, we can use variable addition to do the same operation
l, m, n = "My ", "little ", "pony"
print(l + m + n)


"""
Global is a word often used to refer to the world. In Python, global variable are variables that can be used by any function.
To assign a global variable, simply assign the variable outside of any function.
Creating a variable with the same name as the global variable will not change the global variable or its value, as shown below:
"""

a = "cute"

def foo():
   a = "ugly" # local variable
   print("She is " + a) # prints using local varialbe

foo() # calles function foo()
print("She is " + a) # prints using global variable



""" 
Quiz Time

1. What will the following code output?

2024newyear = "Happy New Year!"

2. What is the value of container?

shelf, container = 100, 20

3. Assign the value -10, 5.5, True, "Yay!" to four variables with different names on one line. Then print each value on one line.
   This means that there should only be two lines of code.
"""

### ANSWER HERE:

# 1. 
# 2. 
# 3. WRITE CODE BELOW:


##


"""
HW: 
Think about different shapes around us. 
How can we tell a computer to draw them? 
What steps do we need? 
"""
