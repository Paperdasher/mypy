##Day3: Python Intro to Libraries and Turtles

"""
In CS, many necessary functions have already been written and programmed for our benefit.
There are many built-in fuctions for the language itself, but there are also many functions/properties we can access.
When we go to the library, we can borrow books about a variety of topics. 
In programming, we can do the same by accessing the specific library which we want to use.
In Python, we typically use the import __ syntax to do so. We can also do import __ as __ to rename the element.
This is typically seen in longer names such as import pandas as pd, import matplotlib as mp.

In our lessons, we will explore the turtle library and use it to visualize our code.

When we want to use methods or functions associated with the library, we'll use the library name then the method.
Ex. turtle.___()
"""


import turtle 

a = turtle.getscreen() ## opens the turtle screen

t = turtle.Turtle() ## this is the turtle we'll use. Here it's being initialized.

"""
In this case, a is the "canvas" and t is the "pen/paintbrush". 
So when we do something to a, it changes the background. 
When we do something to t, it changes how the turtle behaves.
"""

