# Some people are standing in a row in a park. 
# There are trees between them which cannot be moved. 
# Your task is to rearrange the people by their heights in a 
# non-descending order without moving the trees. 
# People can be very tall!

def sortByHeight(a):
    # sort = a  sorted but excluding -1s
    sort = sorted([x for x in a if x!= -1])
    j = 0
    for i in range(len(a)):

        if a[i] != -1:
            a[i] = sort[j]
            j+=1
            
    
    return a
