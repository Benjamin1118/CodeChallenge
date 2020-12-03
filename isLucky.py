#Ticket numbers usually consist of an even number of digits. 
# A ticket number is considered lucky if the sum of the first half of the digits
#  is equal to the sum of the second half.

#Given a ticket number n, determine if it's lucky or not.


def isLucky(n):

# find length of ticket 
    s = str(n)
    length = len(s)
# split it in half.
    half = length//2
    n1 = [int(x) for x in list(s[0:half])]
    n2 = [int(x) for x in list(s[half:length])]
# Sum both halfs
    sum1 = sum(n1)
    sum2 = sum(n2)
# if equal return true
    if sum1 == sum2:
        return True
# else return false
    else:
        return False

