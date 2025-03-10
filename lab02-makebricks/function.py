## Lab02- Make Bricks ##

# This lab is more conceptual than hard core coding. 
# You will have to LOGICALLY think of the solution on paper before coding, coding the solution is not the intent.

# You will first write test cases in a Driver file, provided to you called Driver.py


# Use this function to test how to call different functions in a separate Python file in the same directory
def test(n):
    return n + 1


##############

# You are given a certain number of length 5 blocks (big) and length 1 blocks (small).
# You have to make a goal length of blocks using the big and small blocks.

# input: int small, int big, int goal -> return: boolean
# Small amount of big blocks, large amount of small blocks, true: makeBricks(22, 3, 34)
# Large amount of big blocks, small amount of small blocks, true: makeBricks(4, 7, 24)
# Large amount of big blocks, small amount of small blocks, false: makeBricks(2, 5, 18)

def makeBricks(small, big, goal):
    return False