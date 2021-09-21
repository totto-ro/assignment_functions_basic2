#Countdown
def countDown( num ):
    secuence = []
    for element in range(num, -1, -1):
        secuence.append(element)
    return secuence
num = 9
result = countDown(num)
print(result)

#Print and Return
def printAndReturn( arr ):
    print(arr[0])
    return arr[1]
twoNum = [1, 2]
result = printAndReturn( twoNum )
print(result)

#First Plus Length
def firstPlusLength ( arr ):
    sum = arr[0] + len( arr )
    return sum
numList = [1, 2, 3, 4, 5]
result = firstPlusLength( numList )
print(result)

#Values Greater than Second
def valuesGreaterThanSecond( arr ):
    if len(arr) < 2:
        return False
    newArr = []
    for element in range (0, len(arr), 1):
        if arr[element] > arr[1]:
            newArr.append( arr[element])       
    print(len(newArr))
    return newArr
    
print(valuesGreaterThanSecond([5,2,3,2,1,4]))
print(valuesGreaterThanSecond([3]))

#This Length, That Value
def thisLengthThatValue( length, value ):
    newList = []
    for element in range( 0, length ):
        newList.append(value)
    return newList 
print( thisLengthThatValue(4, 7)) 
print( thisLengthThatValue(6, 2))       
