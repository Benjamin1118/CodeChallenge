#Given two strings, find the number of common characters between them.
def commonCharacterCount(s1, s2):
    # compare and find similar char in each
    # find shorter of s1 and s2
    count = 0
    if len(s1) > len(s2):
        short = s1
        long = s2
    else:
        short = s2
        long = s1
        
    for i in short:
        if i in long:
            count += 1
            short.replace(i,'',1)
            long = long.replace(i,'',1)
            
    return count
