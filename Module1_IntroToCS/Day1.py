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
- Cannot start a name with a number -> cannot have 9students = "students"
- Only contain alpha-numeric characters and underscores(A-z, 0-9, _) -> no name such as yay! = "yay!"
- Case-sensitive -> Hello not = to hello
- No keywords(bool, int, def, etc.) -> cannot be: bool = 3, def = "wrong", int = 3

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


#---------------------------------------#

## str
"""
A String is a type where any character can be written inside a "" or a ''. It's like a conversation, anything can be inside of it.
We can have a string of numbers "12345" or a word "Hello User!" or a combination of both "Hello User 12345!"
Those are some of the glimpse of this data type. We can print literal strings using print(). 

PYTHON IS CASE-SENSITIVE!!! The string "Hello" is not the same as the string "hello"

Multi-line strings can be written using a triple quotation of either type " or '.
"""

#### Try creating a string variable, and printing it. 


"""
Each character in the string has a property called an "index". This means that each character can be referenced using its index.

In the string "Hello!" the H is considered index 0. We always start with the index 0, not 1.
So H is 0, e is 1, ll is 3 and 4, o is 5, ! is index 6. 

We can use indexes to also "slice" strings, meaning we take a certain part of the string we'd like.
We can use the [] to slice, not just for strings but for data structures as well. We'll go over that later.
For now, know that the variable[start(default 0):end(not including)] slices the string. Use the indexes to determine where to start and end.
Also know we can negative index, which means that the last character is -1 and descends going left. Negative indexing starts at -1, not 0.
In the case of "Hello!", ! is also -1, o is -2, and so on. 
"""

####Try to slice any three characters of a string and printing. Do the same but with negative indexing as well.


"""
We can also directly compare str using the == operator to see if they are equal or not.
We can add strings as well, using concatenation. For example, "hello" + " world" would become "hello world"
Concatenation only works with strings in Python though, unlike other languages such as Java.
"""

print("abc" == "ABC") # example of Python being case-sensitive
print('I Love Python!' == "I Love Python!") # since the "" and '' are considered the same in terms of a string, they will be equal
print("Python " + "is" + " fun") # would print "Python is fun", will add the way written so spaces need to be added accordingly
print("My" + "funny" + "friend") # would print "Myfunnyfried" since there are no spaces in the strings



#---------------------------------------#

## float
"""
A float number is like all other numbers, where we have decimal values. It doesn't have to include decimals, but it encompasses all real numbers so that we can do math
that isn't restricted to integers. 
"""

#### Try creating a float variable, and printing it



"""
Usually, homework is a coding using the concepts we go over in session. These are short snippets to help you practice on your own.
Homework is usually in the following four forms:
- Homework file
- Open-ended question, question to think about leading to next session
- Finishing a project
- CodingBat practice

For most homeworks, there will be a separate homework file named DateHW.py. For example, today's homework is in this folder named Day1HW.py.
Please complete these homeworks in the designated homework file so it is clear where you have completed the task. 
It also helps when you do print statements so that material from session isn't included in the printed response. 

For open-ended questions, think about the answer and possible ways of tackling the problem. 
There is no "submission" of this type of homework, rather it is a way for you to keep pondering about CS and think by yourself before presented an algorithm or method.
This helps you better understand concepts, and makes you a better problem-solver, an essential skill in CS.

There will be several projects throughout the term. Projects are a wider scope of material. For instance, there is a project in a couple of lessons that covers the whole second module.
This is a way to better apply a broader idea to practical code, not just snippets for homework to check each individual idea. Applying concepts together is necessary for mastery.
I will give you session time to work on these projects. Since I am giving you session time, I want to help you kick start the project and make sure you're on the right track.
I will only give one session of time per project, so any questions outside of session must be asked through email. 
PLEASE EMAIL ME ASAP WHENEVER YOU HAVE A QUESTION, I will NOT be periodically checking repl.it through the week to see your progress.

CodingBat practice is a great way to tackle algorithm problems and test your proficiency. Usually CodingBat problems need you to return, not print. When you press go, it will test for you.
When stuck, write out your process on paper in forms of English words and diagrams. This will help visualize rather than think in Python terms.
PLEASE REMEMBER TO LOG IN BEFORE WORKING!!! If you do not login, your progress will NOT be saved, and I won't see that you've completed the problems.


I will check homework right before session. 
If you would like to go over something, please let me know AT THE START OF SESSION. If everything is correct, I will assume that you understand and not spend time reviewing. 
"""

## HW: Create a variable of favorite color, number. Print the variables out.
