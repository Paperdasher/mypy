## Day 12: Intro to Data Structures- Lists

"""
When we store data, we have structured formats to streamline our information. 
One common way that we do this is using lists. The most common is a list of integers, but we can have a list of strings as well.

Lists are notated with the square bracket "[]" characters. We separate values using commas.
Ex. ["a", "b", "c"]

We can also have lists inside of lists. The most common is called a 2-D list.
This is commonly used in context of rows and columns. For example, storing information for a bingo card would use 2-D lists for the rows and columns.
When using 2-D lists, the format goes as follows: list[row][column]. It can also be thought of as list[outside][inside].
Ex. [["a", "b", "c"], ["d", "e"]]

To access elements in a list, each element has a property called an index. This is their position in the list, and we use indexing to extract these elements.
Use the name of the list and [index].

Ex. Making a phone call keypad
keypad =
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
["*", 0, "#"]

Above, 2 can be accessed as keypad[0][1], 7 can be accessed as keypad[2][0], "#" can be accessed as keypad[3][2].
If we want a sublist(the 1-D list stored inside of the 2-D list), we may just use list[index]. 
Here, we can use keypad[1] and it would return [4, 5, 6].

List
list.append(value)- adds value to end of list
list.insert(index, value)- inserts value at the index given(not after element at index, but inserted in front)
list.remove(value)- removes value from list
"""

# ----------------------------------------- #

"""
Exercises: Use the given lists per problem(list1 for #1, list2 for #2, etc.), and reach the list given under each problem using list methods.
Use manipulation, DO NOT create a new list with the given values.

1. [5, -4, 9.14, 85, 281, 40012, 74.8, -425]
2. ["hi", "hola", "bonjour", "privet", "bonjourno", "ciao", "konnichiwa", "annyeong haseyo", "bienvenido"]
3. [[1, 3, 2, 4, 5], [6, 7, 8, 9, 10]]
"""

list1 = [5, 10, -4, 9.14, 281, 40012, 74.8]
list2 = ["hi", "hello", "hola", "bonjour", "bonjourno", "konnichiwa", "annyeong haseyo"]
list3 = [[1, 2, 3, 4, 5], [6, 7, 8, 9], ["10", "11", "12"]] //2-D list


# ----------------------------------------- #

## HW: Complete three CodingBat exercises in category "Lists"
