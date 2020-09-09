# 
# a1pr1.py - Assignment 1, Problem 1
#
# Indexing and slicing puzzles
#
# This is an individual-only problem that you must complete on your own.
# 

#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [2, 5, 9] from pi and e
answer0 = [e[0]] + pi[-2:] 

# Solve puzzles 1-4 here:

#puzzle 1
answer1 = e[0:2]

#puzzle 2
answer2 = [pi[4]] + [pi[2]] + [pi[0]] 

#puzzle 3
answer3 = [pi[0]] + [pi[-2]] + [e[-2]]

#puzzle 4
answer4 = e[::-2] + pi[::2]

#
# String puzzles
#

b = 'boston'
u = 'university'
t = 'terriers'

# Example puzzle (puzzle 5)
# Creating the string 'bossy'
answer5 = b[:3] + t[-1] + u[-1]

# Solve puzzles 5-10 here:

#puzzle 6
answer6 = u[0:7] + t[1]

#puzzle 7
answer7 = t[2] + b[1:4] + t[1:3]

#puzzle 8
answer8 = b[0:2] + u[2:7:4] + t[0:3] + b[1] + u[0:7:6]

#puzzle 9
answer9 = (u[-1] + u[4:7:2]) * 3

#puzzle 10
answer10 = t[0:6:2] + u[-4:-1:2]




