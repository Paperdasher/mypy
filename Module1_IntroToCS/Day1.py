##Day1: Intro and Data Types
## W3Schools Explanation: https://www.w3schools.com/python/python_variables.asp

## As you can notice, this is a comment and will not run when called
## Anything after the # symbol is considered a comment for that line
"""
This is a multi-line comment. Python ignores literal strings that are not assigned to a variable. 
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

"""
Variables have variable names. Most languages accept similar standards of names. 
- Start with letter or underscore
- Cannot start a name with a number
- Only contain alpha-numeric characters and underscores(A-z, 0-9, _)
- Case-sensitive
- No keywords(bool, int, def, etc.) 

When assigning variable names, format it as variable_name = variable_value

Ex. sport = "basketball", year = 2024
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


## str
"""
A String is a type where any character can be written inside a "" or a ''. It's like a conversation, anything can be inside of it.
We can have a string of numbers "12345" or a word "Hello User!" or a combination of both "Hello User 12345!"
Those are some of the glimpse of this data type. We can print literal strings using print(). 

PYTHON IS CASE-SENSITIVE!!! The string "Hello" is not the same as the string "hello"

Multi-line strings can be written using a triple quotation of either type " or '.
"""

#### Try creating a string variable, and printing it

"""
We can also directly compare str using the == operator to see if they are equal or not.
We can add strings as well, using concatenation. For example, "hello" + " world" would become "hello world"
Concatenation only works with strings in Python though, unlike other languages such as Java.
"""

print("abc" == "ABC") # example of Python being case-sensitive
print('I Love Python!' == "I Love Python!") # since the "" and '' are considered the same in terms of a string, they will be equal
print("Python " + "is" + " fun") # would print "Python is fun", will add the way written so spaces need to be added accordingly
print("My" + "funny" + "friend") # would print "Myfunnyfried" since there are no spaces in the strings


## int
"""
An int is like the integers you deal with in math class. They don't contain decimals, and can be both negative or positive.
So, 5 is a valid int and so is -2000. 
"""

#### Try creating a int variable, and printing it


## float
"""
A float number is like all other numbers, where we have decimal values. It doesn't have to include decimals, but it encompasses all real numbers so that we can do math
that isn't restricted to integers. 
"""

#### Try creating a float variable, and printing it



"""
HW: Create a variable of favorite color, number. Print the variables out.
"""