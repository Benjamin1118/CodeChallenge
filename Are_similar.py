# Two arrays are called similar if one can be obtained from another 
# by swapping at most one pair of elements in one of the arrays.

# Given two arrays a and b, check whether they are similar.

# Example

# For a = [1, 2, 3] and b = [1, 2, 3], the output should be
# areSimilar(a, b) = true.

# The arrays are equal, no need to swap any elements.

# For a = [1, 2, 3] and b = [2, 1, 3], the output should be
# areSimilar(a, b) = true.

# We can obtain b from a by swapping 2 and 1 in b.

# For a = [1, 2, 2] and b = [2, 1, 1], the output should be
# areSimilar(a, b) = false.

# Any swap of any two elements either in a or in b won't make a and b equal.

def areSimilar(a, b):
    # check if a[i] == b[i]
    # if a[i] != b[i] Swap +=1
    swap = 0
    for i in range(0,len(a)):
        if a[i] == b[i]:
            i +=1
        # check if a[i] is in b
        # if a[i] is not in b return false
        elif a[i] not in b:
            return False
        else:
            swap += 1
    if len(a) == len(b) and sum(a)== sum(b) and swap <= 2:
        return True
    else:
        return False
