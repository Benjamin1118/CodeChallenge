#Given an array of strings, return another array containing all of its longest strings.
def allLongestStrings(inputArray):
    # find longest string in array and return all strings of that len
    #keep longest out of for loop to keep it from changing
    longest = 0
    #finds the longest array in inputArray
    for i in inputArray:
        length = len(i)
        if length > longest:
            longest = length
    #make array to return
    arr = []
    #append all from inputArray where len == longest 
    for i in inputArray:
        if len(i) == longest:
            arr.append(i)
    #return arr
    return arr
    