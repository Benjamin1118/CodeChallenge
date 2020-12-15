# Given an integer n, return the largest number that contains exactly n digits.

# Example

# For n = 2, the output should be
# largestNumber(n) = 99.


def largestNumber(n): 
    b = 9
    a = 9
    for i in range(0,n-1):
        b = str(b)+str(a)
        b = int(b)
    return b
    #another solution
    # return int('9'*n)


n = 5
largestNumber(n)