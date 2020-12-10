# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# Example

# For

# picture = ["abc",
#            "ded"]
# the output should be

# addBorder(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]


def addBorder(picture):
   
    # find size of matrix row & col
    pic = []
    row = len(picture)
    col = len(picture[0])
    
    # create a row of "*" above and below matrix the len(row) + 2
    n_row = "*" *(col+2)
    
    pic.append(n_row)
    for i in range(0,row):
        pic.append("*" + picture[i] + "*")
    pic.append(n_row)
        
    return pic
