finalNumberAscending = int(123456790)
finalNumberDescending = int(9876543211)
def ascendingCount():
    total = 0
    for i in range(1, finalNumberAscending ):
        stringOfNumber = str(i)
        lastDigit = 0
        valid = True
        for digit in range(len(stringOfNumber)):
            intDigit = int(stringOfNumber[digit])
            if intDigit <= lastDigit:
                valid = False
                break
            lastDigit = intDigit
        if(valid):
            total += 1
    return total

def descendingCount():
    total = 0
    for i in range(0, finalNumberDescending):
        stringOfNumber = str(i)
        lastDigit = 10
        valid = True
        for digit in range(len(stringOfNumber)):
            intDigit = int(stringOfNumber[digit])
            if intDigit >= lastDigit:
                valid = False
                break
            lastDigit = intDigit
        if(valid):
            total += 1
    return total

ascendingTotal = ascendingCount()
descendingTotal = descendingCount()

print(f"Ascending Count: {ascendingTotal}")
print(f"Descending Count: {descendingTotal}")
print(f"Descending + Ascending Count: {ascendingTotal + descendingTotal}")
