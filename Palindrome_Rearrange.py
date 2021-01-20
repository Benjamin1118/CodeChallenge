# Given a string, find out if its characters can be rearranged to form a palindrome.

# Example

# For inputString = "aabb", the output should be
# palindromeRearranging(inputString) = true.

# We can rearrange "aabb" to make "abba", which is a palindrome.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string inputString

# A string consisting of lowercase English letters.

# Guaranteed constraints:
# 1 ≤ inputString.length ≤ 50.

# [output] boolean

# true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.

def palindromeRearranging(inputString):
    letters = []
    strike = 0
    for i in inputString:
        if i in letters:
            continue
        elif i not in letters:
            letters.append(i)
            # count = 0
            c = inputString.count(i)
            # for i in inputString:
            #     count += 1
            if c % 2 != 0:
                strike += 1
    if strike >= 2:
        return False
    else:
        return True
        
                
                