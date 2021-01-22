# Given an array of integers, find the maximal absolute difference
# between any two of its adjacent elements.

# Example

# For inputArray = [2, 4, 1, 0], the output should be
# arrayMaximalAdjacentDifference(inputArray) = 3.

def arrayMaximalAdjacentDifference(inputArray):
    m = 0
    x = 0
    for i in inputArray:
        # print(inputArray[x],inputArray[x+1])
        # print(abs(abs(inputArray[x]) - abs(inputArray[x+1])))
        if x == len(inputArray)-1:
            return m
        if abs(inputArray[x] - (inputArray[x+1])) > m:
            m = abs(inputArray[x] - inputArray[x+1])
            x += 1
        else:
            x += 1
        
    return m
