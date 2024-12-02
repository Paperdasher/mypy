##Day 9: Intro to Operations

"""
When we deal with data, many times we need to do mathmatical operations. We can use our everyday math operators for this.
Arithmetic Operators- 
Addition: +
Subtraction: -
Multiplication: *
Division: /
Floor Division: // (15 // 2 = 7, rounds result down to nearest whole num(always int type))
Modulo: %
Exponentiaiton: ** (2**3 = 8)

Add can be used for other types such as strings. We usually dont use the other operators, though(how do you multiply a string to a string??)
"""


"""
Assignment Operators-
Equals: =

We can use special assignment syntax to cut the amount of code we need to write.

+=, -=, *=, /= -> this means add, subtract, ..., a certain value to the variable
Ex. a -= 1 -> subtracts 1 to a, string_name += "abc" -> adds the string "abc" to string_name
This cuts down from writing a = a - 1, and makes our code clearer.

We can do this for any arithmetic operation to assign it to a variable. 

Note: In some languages, ++, --, and similar assignment operators are valid. In Python, they are not allowed.
"""


"""
Comparison Operators-
Equal: ==
Not equal: !=
Greater than: >
Less than: <
Greater than or equal to: >=
Less than or equal to: <=

Always remember that the equals comes after the character. So for assignment and comparison operators, equals always is the last character.

Comparison operators are most frequently used in if statements. They return a boolean value. 
In other languages, they may be embedded in a for loop as the boolean condition. In Python, it will mostly be used in the while loop in the cases of iterating.
"""



"""
Int and Float:

Depending on the language, math operators act differently based on the data type. In Python, it converts the result to the more specific type.

Addition, subtraction, multiplication:
- when using only ints, the result is an int
- when mixing ints and floats, the result is the more specific data type(float)

Division:
- result always a float(even if dividing two ints that are divisible)
Ex. 10 / 2 => 5.0
Ex2. 2/5 => 0.4
Note: In some languages such as Java, int division always results in int division, so 2/5 would result in 0.
"""


#----------------------------------------------------------------------------#


"""
Exercise: For the following problems, write the correct operation. Be careful of order of operations when coding.

1. Add 4 to 2. Then multiply by 6. Subtract 1. Then divide by 5.
2. Take 3 to the power of 3. Then find the whole number result when divided by 4. Take that number and subtract 5.
3. What is the remainder of 329176 divided by 913?
"""


## HW: Make a function that takes a number and adds 5.