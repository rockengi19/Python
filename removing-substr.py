# This function deletes the first substring's occurence from another string

def remove(substr, theStr):
    i = theStr.find(substr)
    if i < 0:
       return theStr
    resultStr = theStr[:i] + theStr[i + len(substr):]
    return resultStr

print(remove('cyc','bicycle'))
print(remove('si','mississipi'))
