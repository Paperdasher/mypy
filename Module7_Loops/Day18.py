##Day 18: Real-life scenario- FizzBuzz

"""
When entering the career of any technical field, they must be proficient in the category the wish to pursue.
For a computer scientist, they need to know at least the basics of programming to be able to write more complex code to help companies or organizations.
In many interviews, especially for technical jobs, interviewers ask a technical question or ask for the interviewee to do a basic sample task.
In CS, many choose to give the FizzBuzz problem. This is a famous problem that tests if an applicant knows the basics of programming.

The problem goes as follows:

Given a list of consecutive integers starting at the start value and up to but not including the end, create a new list in which...
- For multiples of three return "fizz"
- For the multiples of five return "buzz"
- For numbers which are multiples of both three and five return "fizzbuzz"
The function must return a new list of strings with the alteration in place.

Ex: 
fizzBuzz(1, 6) → ["1", "2", "Fizz", "4", "Buzz"]
fizzBuzz(1, 8) → ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7"]
fizzBuzz(1, 11) → ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]
"""

### CODE BELOW ###

# Takes a start and end val, returns new String list where mult of 3 are replaced by "fizz", mult of 5 by "buzz", and mult of 15 by "fizzbuzz"
#int start and end -> String list
def fizzbuzz(start, end):