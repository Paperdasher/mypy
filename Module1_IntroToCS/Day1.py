##Day1: Intro and Data Types
## W3Schools Explanation: https://www.w3schools.com/python/python_variables.asp

## As you can notice, this is a comment and will not run when called
## Anything after the # symbol is considered a comment for that line
"""
This is a multi-line comment. This can be done using three quotes to start and to end. 
You can find more info about comments at this link: https://www.w3schools.com/python/python_comments.asp
"""

"""
In Python, there are multiple data types. The most common ones are:
- str(String)
- int(Integer)
- float(Decimal)
- bool(Boolean)
- list
- dict(Dictionary)
- range
"""



## str
"""
A String is a type where any character can be written inside a "" or a ''. It's like a conversation, anything can be inside of it.
We can have a string of numbers "12345" or a word "Hello User!" or a combination of both "Hello User 12345!"
Those are some of the glimpse of this data type. We can print literal strings using print(). 

PYTHON IS CASE-SENSITIVE!!! The string "Hello" is not the same as the string "hello"

Multi-line strings can be written just like a comment. These comments are technically multi-line strings, but since they aren't printed
won't affect the code.
"""


a = "Hello"
print("Hola")
print('Bonjour')
print(a)

"""
We can also directly compare str using the == operator to see if they are equal or not.
"""

print("abc" == "ABC") # example of Python being case-sensitive
print('I Love Python!' == "I Love Python!") # since the "" and '' are considered the same in terms of a string, they will be equal

## int
"""
An int is like the integers you deal with in math class. They don't contain decimals, and can be both negative or positive.
So, 5 is a valid int and so is -2000. 
"""

b = 5
c = -2000
print(b)
print(c)


## float
"""
A float number is like all other numbers, where we have decimal values. It doesn't have to include decimals, but it encompasses all real numbers so that we can do math
that isn't restricted to integers. 
"""

d = 10.0  # This is an example of a float number that doesn't have "decimal points"
e = -24.563 # float numbers can be negative
print(d)
print(e)

## bool
"""
A boolean is a concept of True and False. If somebody asks you "Can humans time-travel?" your answer most likely will be "No."
We can assess that this question was a True or False question, so your answer in boolean terms would be false.
Most terms in Python will return True if you put it in boolean terms. But, some values are considered false.
False, None, 0, "", (), [], {} will all return false. Basically, empty elements, the boolean False, None, and 0 will give you False.
This means that, when we deal with numbers, we can use 0 and 1 as binary terms to return True and False values.
"""



## Print Statements
"""
Printing! The only way the system outputs something we can see is through the built-in print() function.
This allows us to output whatever is inside the (). 
Note: Trying to print a variable without defining it will result in an error. 
"""

#print(f) will result in an error
print("f") # will be considered as a string and therefore output f
print(123) # will print the int 123
print(123.05) # will print the float 123.05
print(bool(0)) # will print False, this is something called Type Casting. 