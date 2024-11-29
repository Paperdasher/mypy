##Day 2: Type Casting, Advanced Data Types


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



