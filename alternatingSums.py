# Several people are standing in a row and need to be divided into two teams. 
# The first person goes into team 1, the second goes into team 2, 
# the third goes into team 1 again, the fourth into team 2, and so on.

# You are given an array of positive integers - the weights of the people. 
# Return an array of two integers, where the first element is the total weight of team 1, 
# and the second element is the total weight of team 2 after the division is complete.


def alternatingSums(a):
    # make new array with 2 indexes
    b = [0,0]
    # if index i is odd add to first "new" index
    for i in range(len(a)):
        if i % 2 == 0:
            b[0] += a[i]
    # if index is even add to second "new" index
        else:
            b[1] += a[i]

    # return array with those two sums
    return b



# Example

# For a = [50, 60, 60, 45, 70], the output should be
# alternatingSums(a) = [180, 105].

# Input:
# a: [50, 60, 60, 45, 70]
# Expected Output:
# [180, 105]