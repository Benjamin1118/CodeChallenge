# You are given an array of integers. On each move you are allowed to increase,
#  exactly one of its element by one. Find the minimal number of moves required
# to obtain a strictly increasing sequence from the input.

# Example

# For inputArray = [1, 1, 1], the output should be
# arrayChange(inputArray) = 3.

# Input/Output

# [execution time limit] 4 seconds (py3)

def arrayChange(inputArray):
    move = 0
    turn = inputArray[0]
    for i in inputArray[1:]:
        if i <= turn:
            move += turn-i+1
            turn += 1
        else:
            turn = i
    return move
    
    # working code that will actually change inputArray to an ascending array, 
    # but times out on bigger tests.
    # move = 0
    # turn = 0
    # while turn < len(inputArray)-1:
    #     if inputArray[turn] < inputArray[turn+1]:
    #         turn += 1
        
    #     else: # inputArray[turn] <= inputArray[turn+1]:
    #         inputArray[turn+1] += 1
    #         move += 1
        
    # return move
    
