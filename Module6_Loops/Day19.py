## Day 19 & 20: Sorting Algorithms

"""
Now that we're comfortable with Data Structures and Loops, let's put them to test together.
When we have a list of numbers, it can be beneficial to have them sorted. When we say "sorted", we usually mean in acsending order.
There are many algorithms in the world to accomplish this. Although most likely the three worst, let's practice using algorithms designed for educational purposes.
"""

bubble = """
- Bubble sort

Set the end to length-1.

1. compare list[i] with list[i+1], if they are not in order swap them.
2. Increase i
3. Repeat steps 1 and 2 until you reach the end index.
4. Decrease the end by 1.
5. When there was at least one swap (use a variable for this aka a flag), repeat from step 1 again. This makes it so when there are no swaps, the algorithm stops early.
"""

selection = """
- Selection sort

1. Scan the entire array from the beginning element to the "ending" index for the maximum value.
2. Swap the "ending" element with max value
3. Reduce the "ending" index by 1 since the current ending index has the correct value.
4. Repeat from step 1 until there is only 1 element left.

In other words:
Given list = [64, 25, 12, 22, 11];

Find the maximum element in list[0...4] and place it at end of [0...4].
11, 25, 12, 22, |64|

Find the maximum element in list[0...3] and place it at the end of that sub-list[0...3]
11, 22, 12, |25, 64|

Find the maximum element in list[0...2] and place it at the end of that sub-list[0...2]
11, 12, |22, 25, 64|

Find the maximum element in list[0...1] and place it at the end of that sub-list[0...1]
11, |12, 22, 25, 64|
"""

insertion = """
- Insertion sort

1. For each element of the list starting with index 1.
2. Push the element back into the previous elements.
3. "Pushing it back" means as long as the element is smaller than the previous, shift (copy) the larger value one index higher, 
    then look at the value previous to the original position of the larger value.
4. When the element is no longer smaller the previous or you reach index 0, copy the element back into the list.
Note: Do not make a series of swaps. Store the key element in a temporary location and place it into the list once.

Example:
[12, 11, 13, 5, 6]
Let us loop for i = 1 (second element of the list) to 4 (last element of the list)

i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12
11, 12, 13, 5, 6

i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13
11, 12, 13, 5, 6

i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position.
5, 11, 12, 13, 6

i = 4. 6 will move to position after 5, and elements from 11 to 13 will shift one position ahead of their current position.
5, 6, 11, 12, 13 
"""

"""
PLEASE DO NOT CHANGE THE FUNCTION NAMES. You do NOT need helper functions for this task.
You may work on the functions in the separately provided file. You should also test your functions in that file.
After you are sure your code works, you may paste it below.
"""

print(bubble)
print(selection)
print(insertion)

## BUBBLE SORT:

def bubble():
    pass

## SELECTION SORT:

def selection():
    pass

## INSERTION SORT:

def insertion():
    pass
